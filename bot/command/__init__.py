'''
Created on 16 Sep 2019

@author: jwendling
'''


class Command(object):
    '''
    This is the abstract class for all bot commands!
    '''

    @staticmethod
    def get_identifier() -> list:
        raise Exception("Implement me!")
        return []

    @staticmethod
    def get_description() -> str:
        raise Exception("Implement me!")
        return ("None")

    @staticmethod
    def process_message(message) -> str:
        raise Exception("Implement me!")
        return ("None")