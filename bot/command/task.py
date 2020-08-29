'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command
from bot.vars.application import CONTEXT_TASK
from model.task import TaskModel

class TaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['task', 't']

    @staticmethod
    def get_description() -> str:
        return "*This command will handle all of the operations regarding a task*\n\n" \
               "**Subcommands:** [new|edit|close|resume|project|tag]\n\n" \
               "For more details ask help task"

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