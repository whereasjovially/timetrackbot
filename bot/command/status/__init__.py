'''
Created on 18 Sep 2019

@author: jwendling
'''

from bot.command import Command


class StatusCommand(Command):
    '''
    Bot Command for showing current status
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['status', 'stat']

    @staticmethod
    def get_description() -> str:
        return "`[?id]` *Show status displays current task, working hours track*"

    @staticmethod
    def process_message(message, app) -> (str, str):
        # Extract from message.text

        # To-Do Daily Summary

        # app.current_object.add_content(service)
        return ("", app.current_context)