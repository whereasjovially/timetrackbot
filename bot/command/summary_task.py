'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command

class SummaryTaskCommand(Command):
    '''
    Bot Command for showing a summary of all tasks per day/week
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['summary']

    @staticmethod
    def get_description() -> str:
        return "Shows the summary for day, week or last xx" \
               "***Subcommands:*** [today|week|month|date|project]"

    @staticmethod
    def process_message(message, app) -> (str, str):
        # Extract from message.text

        # To-Do Daily Summary
        
        #app.current_object.add_content(service)
        return("", app.current_context)