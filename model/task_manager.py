'''
Created on 16 Sep 2019

@author: jwendling
'''

#from gql import gql, Client
#from gql.transport.requests import RequestsHTTPTransport

class TaskManager(object):
    '''
    Connection Manager for Task Model
    We could also create other connection model if we are going to
    support direct database access!
    
    Think about something like this:
    
    AbstractManager
     -> GQL_Manager
     -> Mongo_Manager
     
     # query = gql("""
                {
                    pokemon(name: "Pikachu") {
                        attacks {
                            special {
                                name
                            }
                        }
                    }
                }
                """)
    '''

    def __init__(self, config: dict):
        '''
        Constructor
        '''
        #self.gql_client = self.get_gql_client(config['URL'])


    # def get_gql_client(self, graphql_api_url, ):
    #
    #     _transport = RequestsHTTPTransport(
    #         url=graphql_api_url,
    #         use_json=True,
    #     )
    #
    #     client = Client(
    #         transport=_transport,
    #         fetch_schema_from_transport=True,
    #     )
    #     return client

    # def execute_query(self, query: str):
    #     self.gql_client.execute(query)

    # ------------------------------------------------------- Methods/Functions
    
    # def get_object(self, _id: int):
    #     # Call GraphQL for Object
    #
    #     # To-Do send API request and create a Task Model
    #
    #     return None
    #
    # def update_or_create(self, _title: str):
    #
    #     # To-Do Take a TaskModel and either create
    #     # it or update
    #
    #     return None
    #
    # def save_object(self, _obj) -> int:
    #     pass
    #
    # def exists(self, title: str):
    #     # Check if an TaskModel already exists
    #     # Get by Name!
    #     pass