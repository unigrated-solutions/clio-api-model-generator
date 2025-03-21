from dataclasses import dataclass
from typing import Optional, List, Literal, Any
import datetime

@dataclass
class Account:
    id: Optional[int] = None
    firm_name: Optional[str] = None

@dataclass
class Contact:
    clio_id: Optional[int] = None
    created_at: Optional[datetime.datetime] = None
    emails: Optional[List[str]] = None
    id: Optional[int] = None
    matters: Optional[List[Any]] = None
    name: Optional[str] = None
    phone_numbers: Optional[List[str]] = None
    status: Optional[Literal['Unassigned', 'Lead', 'Client', 'Did Not Hire']] = None
    type: Optional[Literal['Company', 'Person']] = None
    updated_at: Optional[datetime.datetime] = None

@dataclass
class CustomAction:
    created_at: Optional[datetime.datetime] = None
    id: Optional[int] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[Literal['matters/show']] = None
    updated_at: Optional[datetime.datetime] = None

@dataclass
class ErrorDetail:
    message: str
    status: str

@dataclass
class Error:
    error: Any

@dataclass
class InboxLead:
    created_at: Optional[datetime.datetime] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    state: Optional[Literal['ignored', 'untriaged']] = None
    updated_at: Optional[datetime.datetime] = None

@dataclass
class Matter:
    created_at: Optional[datetime.datetime] = None
    id: Optional[int] = None
    description: Optional[str] = None
    clio_id: Optional[int] = None
    location: Optional[str] = None
    primary_contact: Optional[Any] = None
    status: Optional[Literal['Newly Added', 'Consult Scheduled', 'Pending Engagement']] = None
    status_category: Optional[Literal['intake', 'hired', 'declined']] = None
    type: Optional[str] = None
    updated_at: Optional[datetime.datetime] = None

@dataclass
class MatterId:
    id: Optional[int] = None

@dataclass
class Note:
    body: Optional[str] = None
    created_at: Optional[datetime.datetime] = None
    id: Optional[int] = None
    subject: Optional[str] = None
    updated_at: Optional[datetime.datetime] = None

@dataclass
class User:
    account: Optional[Any] = None
    created_at: Optional[datetime.datetime] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    last_name: Optional[str] = None
    updated_at: Optional[datetime.datetime] = None

