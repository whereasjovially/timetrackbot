'''
Created on 01 Sep 2020

@author: jwendling
'''

from bot.command import Subcommand
from bot.vars.application import CONTEXT_NONE


class EndWorktimeCommand(Subcommand):
    '''
    Ending Worktime
    '''

    @staticmethod
    def get_identifier() -> str:
        return 'end'

    @staticmethod
    def process_message(message, app) -> (str, str):
        # ToDo: End workingtime tracking
        return (f"Starting working hour track at TIME", app.current_context)