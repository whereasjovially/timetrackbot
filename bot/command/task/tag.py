'''
Created on 01 Sep 2020

@author: jwendling
'''

from .. import Subcommand
from bot.vars.application import CONTEXT_NONE


class TagTaskCommand(Subcommand):
    '''
    Adds or removes tags from current task
    e.g. task tag security adds the tag security if its already applied then it will remove it -> "trigger on/off"
    '''

    @staticmethod
    def get_identifier() -> str:
        return 'tag'

    @staticmethod
    def process_message(message, app) -> (str, str):
        # ToDo: Add tagging
        return (f"TaskTag", app.current_context)