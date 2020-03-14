'''
Created on 16 Sep 2019

@author: jwendling
'''

class WorkingHoursMongoManager(object):
    '''
    Connection Manager for direct mongo db access
    '''

    def __init__(self, config: dict):
        '''
        Constructor
        '''
        pass


    def execute_query(self, query: str):
        pass

    # ------------------------------------------------------- Methods/Functions
    
    def get_object(self, _id: int):
        return None

    def update_or_create(self, _title: str):
        return None
    
    def save_object(self, _obj) -> int:
        pass
    
    def exists(self, title: str):
        pass