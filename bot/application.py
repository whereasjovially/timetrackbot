'''
Created on 17 Sep 2019

@author: jwendling
'''

import os
from bot.command import Command
from bot.command.task import TaskCommand
from bot.command.help import HelpCommand
from bot.command.summary import SummaryCommand
from bot.command.status import StatusCommand
from bot.command.worktime import WorktimeCommand
from bot.webhook import Webhook as BotWebhook
from webexteamssdk import WebexTeamsAPI
from webexteamssdk import Webhook
from _collections import OrderedDict
import yaml
import re
from model.task_manager import TaskManager
import time
from bot.vars.application import CONTEXT_TASK, CONTEXT_NONE, CONTEXT_WORKTIME


MESSAGE_TIMEOUT = 2


class Application(object):
    '''
    Init Configuration, Creating WebEx API and so on
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
        # Load configvars
        self.config = self.init_config()

        # Defining vars
        self.commands = {}
        self.api = WebexTeamsAPI(self.config['BOT_AUTH_TOKEN'])
        self.webhook = BotWebhook(self.api, self.config['WEBHOOK_SETTINGS'])
        self.bot = self.api.people.me()
        self.current_context = CONTEXT_NONE
        self.current_task = None
        self.previous_task = None
        self.user = None
        #self.task_manager = TaskManager(self.config['GRAPHQL'])
        self.message_trigger = False
        
        # Preprocessing initial data
        self.init_commands()
        self.webhook.create()


    # INIT FUNCTIONS -------------------------------------------------------- #    

    def init_commands(self):
        self.register_cmd(WorktimeCommand)
        self.register_cmd(TaskCommand)
        self.register_cmd(SummaryCommand)
        self.register_cmd(StatusCommand)

    def init_config(self):
        '''
        Loads a environment yaml file to include static configuration variables
        '''
        # To-Do: File Exists and is YML
        config = yaml.load(open('meta/environment.yml'), Loader=yaml.BaseLoader)

        # Overwrite config settings by os.environment
        if 'TARGET_URL' in os.environ:
            config['WEBHOOK_SETTINGS']['TARGET_URL'] = os.environ['TARGET_URL']
        if 'BOT_AUTH_TOKEN' in os.environ:
            config['BOT_AUTH_TOKEN'] = os.environ['BOT_AUTH_TOKEN']
        if 'BOT_ID' in os.environ:
            config['BOT_ID'] = os.environ['BOT_ID']
        if 'BOT_USERNAME' in os.environ:
            config['BOT_USERNAME'] = os.environ['BOT_USERNAME']

        return config


    # GENERAL FUNCTIONS ----------------------------------------------------- #
    
    def process_webhook(self, json) -> str:
        webhook_obj = Webhook(json)
        message = self.api.messages.get(webhook_obj.data.id)
        person = self.api.people.get(message.personId)
        self.user = message.personEmail
        
        # Loop avoidance!
        if message.personId == self.bot.id:
            # Avoid getting spamed!
            # Just pause some seconds between commands
            time.sleep(MESSAGE_TIMEOUT)
            self.message_trigger = False
            return("Do nothing cause the message was sent by myself!")

        if self.message_trigger:
            # Add User to just block this one!
            return("Do nothing cause we already processing a message")
        self.message_trigger = True

        # Authorization check
        if message.personEmail.lower() not in self.config['AUTHORIZED_USERS']:
            result = (f"Hi {person.displayName} ({message.personEmail}), you are not authorized using this application!")
        else:
            result = self.process_message(message)
            time.sleep(MESSAGE_TIMEOUT)
            self.message_trigger = False
        # If result is empty then skip response!
        if result is not None and bool(result):
            self.api.messages.create(webhook_obj.data.roomId, markdown=result)
        return("OK")

    def process_message(self, message):
        # Note: For now I will keep the context mode to be able to use different contexts in the future
        # but currently we will only use one context which is the default
        for identifier in self.commands[self.current_context]:
            
            p = re.compile(f"^{identifier.strip()}")
            match = p.match(message.text.lower())
            
            if match:
                command_obj = self.commands[self.current_context][identifier]
                msg, context = command_obj.process_message(message.text, self)
                self.current_context = context
                return msg
        
        result, context = HelpTaskCommand.process_message(None, self)
        return result

    def register_cmd(self, command: Command, context: str = CONTEXT_NONE):
        # Add Context hierachy to commands if not already done
        if context not in self.commands:
            self.commands[context] = OrderedDict()
        # Add all commands(identifiers) to the dict
        for identifier in command.get_identifier():
            self.commands[context][identifier] = command
