'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_NONE
import datetime

class CloseTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['ct', 'close', 'stop']

    @staticmethod
    def get_description() -> str:
        return "Stopping current task!"

    @staticmethod
    def process_message(message, app) -> (str, str):
        """
        Close current task and set it as prev task for
        further needs like continuing
        """
        task_id = app.current_task.end_task()
        app.previous_task = app.current_task
        app.current_task = None
        
        return(f"Closed Task #{task_id}", CONTEXT_NONE)