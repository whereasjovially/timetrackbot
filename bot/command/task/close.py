'''
Created on 1 Sep 2020

@author: jwendling
'''

from bot.command import Subcommand
from bot.vars.application import CONTEXT_NONE
import datetime

class CloseTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> str:
        return 'close'

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