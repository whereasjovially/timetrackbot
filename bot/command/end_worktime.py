'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_TASK
from model.task import TaskModel

class EndWorktimekCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['end', 'pause', 'break']

    @staticmethod
    def get_description() -> str:
        return "Stops the current working hours track to finish the day or switching to pause :-)"

    @staticmethod
    def process_message(message, app) -> (str, str):
        
        # if app.current_task is not None:
        #     print("Closed current Task!")
        #     app.current_task.end_task()
        #     app.previous_task = app.current_task
        #     app.current_task = None
        #
        task = TaskModel(app.task_manager)
        # To-Do
        task.title = "Extract from Message"
        task.user = app.user
        task.save()
        app.current_object = task
        
        return(f"Finish current working hour track - Duration TIME!", app.current_context)