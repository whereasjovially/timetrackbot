# -*- coding: utf-8 -*-

'''
Created on 09 Sep 2020

@author: jwendling
'''

import json
import logging
import requests
import urllib3

URL_BASE = "https://api.clockify.me/api/v1"
URL_REPORT = "https://reports.api.clockify.me/v1"


class ClockifyAPI(object):

    # API Paths
    WORKSPACE_PATH = f"/workspaces"
    PROJECT_PATH = f"/workspaces/{workspaceId}/projects"
    TASK_PATH = f"/workspaces/{workspaceId}/projects/{projectId}/tasks"

    def __init__(self, _api_key:str):

        self.api_key = _api_key

    # Common -----------------------------------------------------------------------------------------------------------

    def login(self):
        pass

    # WORKSPACE --------------------------------------------------------------------------------------------------------

    def get_workspaces(self) -> list:
        '''
        Retrieves a list of all associated workspaces

        :return: list of workspaces
        '''
        pass


    # PROJECTS ---------------------------------------------------------------------------------------------------------


    # TASKS ------------------------------------------------------------------------------------------------------------
    '''
    TASK API Calls

    METHODS:
        - GET: Retrieve Task
        - POST: Create new
    
    '''

    def create_task(self, name: str) -> str:
        '''
        RESPONSES:
            201 Created
            400 Bad Request- Task with that name already exists on project, or specified project doesn't exist

        :param name: task name
        :return: task id
        '''
        pass

if __name__ == '__main__':
    # Local Tests

    '''
    Example
    curl -H "content-type: application/json" -H "X-Api-Key: yourAPIkey" -X GET https://api.clockify.me/api/v1/user
    '''

    api_key = "X0Oqqn0mRCv1RdB2"

    api = ClockifyAPI(api_key)

    print(api.get_workspaces())