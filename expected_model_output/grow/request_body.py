from dataclasses import dataclass
from typing import Optional, List, Literal
import datetime

@dataclass
class Contactnote_create_RequestBody_Data:
    body: str
    subject: str

@dataclass
class Contactnote_create_RequestBody:
    data: Contactnote_create_RequestBody_Data

@dataclass
class Customaction_create_RequestBody_Data:
    label: str
    target_url: str
    ui_reference: Literal['matters/show']

@dataclass
class Customaction_create_RequestBody:
    data: Customaction_create_RequestBody_Data

@dataclass
class Inboxlead_create_RequestBody_Data:
    first_name: str
    from_message: str
    from_source: str
    last_name: str
    referring_url: str
    email: Optional[str] = None
    phone_number: Optional[str] = None

@dataclass
class Inboxlead_create_RequestBody:
    data: Inboxlead_create_RequestBody_Data

@dataclass
class Matternote_create_RequestBody_Data:
    body: str
    subject: str

@dataclass
class Matternote_create_RequestBody:
    data: Matternote_create_RequestBody_Data

