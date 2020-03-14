'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_TASK

class ServiceTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['service']

    @staticmethod
    def get_description() -> str:
        return "Sets the service id for the current task"

    @staticmethod
    def process_message(message, app) -> (str, str):
        # Extract from message.text
        
        service = message.text
        for identifier in ServiceTaskCommand.get_identifier():
            service = service.replace(identifier, "")
        
        app.current_object.add_content(service)
        return("", CONTEXT_TASK)