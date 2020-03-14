'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_TASK
from model.task import TaskModel

class ContinueTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['continue', 'cont']

    @staticmethod
    def get_description() -> str:
        return "Continues the previous task and switching to Context Task."

    @staticmethod
    def process_message(message, app) -> (str, str):
        """
        Takes the prev tasks and creates a new one with the same
        settings except content!
        """
        
        if app.current_object is not None:
            raise Exception("Not call continue within the task context!")
        
        task = TaskModel(app.task_manager)
        task.title = app.previous_object.title
        task.user = app.previos_object.user
        task.service = app.previous_object.service
        task.save()
        app.current_object = task
        
        return(f"Continued paused task with new id {task.id}!", CONTEXT_TASK)