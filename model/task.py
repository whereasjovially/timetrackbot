'''
Created on 16 Sep 2019

@author: jwendling
'''

from datetime import datetime
import model.task_manager as task_manager

class TaskModel(object):
    '''
    This Taskmodel is a wrapper which calls the middleware API
    '''

    def __init__(self, manager: task_manager.TaskManager):
        '''
        Constructor
        '''
        # Mgmt
        self.manager = manager
        
        # Model Variables
        self.id = None
        self.title = None
        self.service = None
        self.content = []
        self.user = None
        self.start_date = datetime.now()
        self.end_date = None
    
    # ------------------------------------------------------- Methods/Functions
    
    def create(self) -> int:
        '''
        Starts a new task and returns the task_id
        '''
        # To-Do: Generate new GraphQL Object
        # Return ID and set it
        return 1
    
    def end_task(self) -> int:
        '''
        Quits current or given task and return task_id
        '''
        self.end_date = datetime.now()
        # To-Do: Send data to GraphQL
        return self.id

    def save(self) -> int:
        return self.manager.save_object(self)

    def add_content(self, text: str):
        self.content.append(text)
