'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_TASK

class ContentTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['.*']

    @staticmethod
    def get_description() -> str:
        return "Adds any message to the content of the current task"

    @staticmethod
    def process_message(message, app) -> (str, str):
        # Do not save for each content. It should be ok
        # if we save on pause/end
        
        # To-Do: Add Security and add input validation prob on model and not here
        app.current_object.add_content(message)
        return("", CONTEXT_TASK)