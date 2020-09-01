'''
Created on 18 Sep 2019

@author: jwendling
'''

from . import Command

class HelpTaskCommand(Command):
    '''
    Bot Command for creating a new task
    '''

    @staticmethod
    def get_identifier() -> list:
        return ['help', '\?']

    @staticmethod
    def get_description() -> str:
        return "Adds any message to the content of the current task"

    @staticmethod
    def process_message(message, app) -> (str, str):
        # Do not save for each content. It should be ok
        # if we save on pause/end
        
        # To-Do: Add Security and add input validation prob on model and not here
        
        #app.current_object.add_content(message.text)
        
        used_commands = []
        
        output = "## I am helping you..."
        output+= "\n\n---\n\n"
        # output+= f"*Current Context: {app.current_context}*\n\n"
        # output+= "\n\n---\n\n"
        output+= "The following commands are available in the current context:\n\n"
        
        for cmd in app.commands[app.current_context]:
            
            cmd_obj = app.commands[app.current_context][cmd]
            cmds_string = ", ".join(cmd_obj.get_identifier())
            
            if cmds_string not in used_commands:
                output+=(f"\n\nCommands: `{cmds_string}` {cmd_obj.get_description()} \n\n")
                used_commands.append(cmds_string)
        
        return(output, app.current_context)