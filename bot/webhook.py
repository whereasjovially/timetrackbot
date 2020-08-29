'''
Created on 19 Sep 2019

@author: jwendling
'''

from webexteamssdk import WebexTeamsAPI

class Webhook(object):
    '''
    Manage WebEx Webhooks for the Bot
    '''


    def __init__(self, api: WebexTeamsAPI, config: dict):
        '''
        Constructor
        '''
        self.api = api
        self.config = config
        
    def create(self) -> bool:
        
        # Add logging
        if self.config['TARGET_URL'] is None:
            return False
        
        # delete old webhook if its exist!
        self.delete_all_webhooks()
        
        # create new one!
        webhook = self.api.webhooks.create(
            name=self.config['NAME'],
            targetUrl="".join([self.config['TARGET_URL'],
                               self.config['URL_PATH']]),
            resource=self.config['RESOURCE'],
            event=self.config['EVENT']
            )
        print(f"Created Webhook {webhook.id} on {self.config['TARGET_URL']}")
        return True
        
    
    def delete_all_webhooks(self) -> bool:
        webhooks = self.api.webhooks.list()
        
        for webhook in webhooks:
            print(f"Delete Webhook {webhook.id}")
            self.api.webhooks.delete(webhook.id)
