from dataclasses import dataclass
from typing import Optional, List, Literal
import datetime

@dataclass
class Contact_index_Query:
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    query: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

@dataclass
class Contact_show_Query:
    id: int

@dataclass
class Contactnote_index_Query:
    contact_id: int
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

@dataclass
class Contactnote_create_Query:
    contact_id: int

@dataclass
class Customaction_index_Query:
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

@dataclass
class Customaction_destroy_Query:
    id: int

@dataclass
class Inboxlead_index_Query:
    state: Literal['ignored', 'untriaged']
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    query: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

@dataclass
class Inboxlead_show_Query:
    id: int

@dataclass
class Matter_index_Query:
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

@dataclass
class Matter_show_Query:
    id: int

@dataclass
class Matternote_index_Query:
    matter_id: int
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

@dataclass
class Matternote_create_Query:
    matter_id: int

@dataclass
class User_index_Query:
    created_since: Optional[datetime.datetime] = None
    ids__: Optional[int] = None
    page_token: Optional[str] = None
    updated_since: Optional[datetime.datetime] = None

