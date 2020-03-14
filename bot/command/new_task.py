'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_TASK
from model.task import TaskModel

class NewTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['task', 'nt']

    @staticmethod
    def get_description() -> str:
        return "Creating a new Task and returing the id of the new task. If nessecary the current task will be stopped. Switching to Context Task."

    @staticmethod
    def process_message(message, app) -> (str, str):
        
        if app.current_task is not None:
            print("Closed current Task!")
            app.current_task.end_task()
            app.previous_task = app.current_task
            app.current_task = None
        
        task = TaskModel(app.task_manager)
        # To-Do
        task.title = "Extract from Message"
        task.user = app.user
        task.save()
        app.current_object = task
        
        return(f"Generated new task #{task.id}!", CONTEXT_TASK)