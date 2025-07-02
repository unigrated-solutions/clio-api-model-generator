from typing import Dict, Type, Optional
from models.query import *  # Import all query models
from models.request_body import *  # Import all request body models
from models.fields import *

class Endpoints:
    """
    Registry for storing endpoint metadata, including paths,
    query models, and request body models.
    """

    registry: Dict[str, Dict[str, Optional[Type]]] = {}

    @classmethod
    def initialize_registry(cls):
        """
        Initialize the endpoint registry dynamically.
        """
        cls.registry['Contact_index'] = {
            'path': '/contacts',
            'method': 'GET',
            'query_model': Contact_index_Query,
            'request_body_model': None,
            'field_model': Contact_Fields
        }
        cls.registry['Contact_show'] = {
            'path': '/contacts/{id}',
            'method': 'GET',
            'query_model': Contact_show_Query,
            'request_body_model': None,
            'field_model': None
        }
        cls.registry['Contactnote_index'] = {
            'path': '/contacts/{contact_id}/notes',
            'method': 'GET',
            'query_model': Contactnote_index_Query,
            'request_body_model': None,
            'field_model': Note_Fields
        }
        cls.registry['Contactnote_create'] = {
            'path': '/contacts/{contact_id}/notes',
            'method': 'POST',
            'query_model': Contactnote_create_Query,
            'request_body_model': Contactnote_create_RequestBody,
            'field_model': None
        }
        cls.registry['Customaction_index'] = {
            'path': '/custom_actions',
            'method': 'GET',
            'query_model': Customaction_index_Query,
            'request_body_model': None,
            'field_model': CustomAction_Fields
        }
        cls.registry['Customaction_create'] = {
            'path': '/custom_actions',
            'method': 'POST',
            'query_model': None,
            'request_body_model': Customaction_create_RequestBody,
            'field_model': None
        }
        cls.registry['Customaction_destroy'] = {
            'path': '/custom_actions/{id}',
            'method': 'DELETE',
            'query_model': Customaction_destroy_Query,
            'request_body_model': None,
            'field_model': None
        }
        cls.registry['Inboxlead_index'] = {
            'path': '/inbox_leads',
            'method': 'GET',
            'query_model': Inboxlead_index_Query,
            'request_body_model': None,
            'field_model': InboxLead_Fields
        }
        cls.registry['Inboxlead_create'] = {
            'path': '/inbox_leads',
            'method': 'POST',
            'query_model': None,
            'request_body_model': Inboxlead_create_RequestBody,
            'field_model': None
        }
        cls.registry['Inboxlead_show'] = {
            'path': '/inbox_leads/{id}',
            'method': 'GET',
            'query_model': Inboxlead_show_Query,
            'request_body_model': None,
            'field_model': None
        }
        cls.registry['Matter_index'] = {
            'path': '/matters',
            'method': 'GET',
            'query_model': Matter_index_Query,
            'request_body_model': None,
            'field_model': Matter_Fields
        }
        cls.registry['Matter_show'] = {
            'path': '/matters/{id}',
            'method': 'GET',
            'query_model': Matter_show_Query,
            'request_body_model': None,
            'field_model': None
        }
        cls.registry['Matternote_index'] = {
            'path': '/matters/{matter_id}/notes',
            'method': 'GET',
            'query_model': Matternote_index_Query,
            'request_body_model': None,
            'field_model': Note_Fields
        }
        cls.registry['Matternote_create'] = {
            'path': '/matters/{matter_id}/notes',
            'method': 'POST',
            'query_model': Matternote_create_Query,
            'request_body_model': Matternote_create_RequestBody,
            'field_model': None
        }
        cls.registry['User_index'] = {
            'path': '/users',
            'method': 'GET',
            'query_model': User_index_Query,
            'request_body_model': None,
            'field_model': User_Fields
        }
        cls.registry['User_who_am_i'] = {
            'path': '/users/who_am_i',
            'method': 'GET',
            'query_model': None,
            'request_body_model': None,
            'field_model': None
        }

        # Initialize the registry
Endpoints.initialize_registry()
