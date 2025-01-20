from dataclasses import dataclass
from typing import Optional
from models.schemas import *

@dataclass
class ErrorDetail_Fields:
    pass

@dataclass
class Error_Fields:
    pass

@dataclass
class IdsResponse_Fields:
    pass

@dataclass
class Comment_Fields:
    # Fields directly copied from Comment_base
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    creator: Optional[User_base] = None
    document_version: Optional[DocumentVersion_base] = None

@dataclass
class DocumentArchive_Fields:
    # Fields directly copied from DocumentArchive_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    state: Optional[str] = None
    message: Optional[str] = None

@dataclass
class DocumentAutomation_Fields:
    # Fields directly copied from DocumentAutomation_base
    id: Optional[int] = None
    etag: Optional[str] = None
    state: Optional[str] = None
    export_formats: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None
    document_template: Optional[DocumentTemplate_base] = None
    documents: Optional[Document_base] = None

@dataclass
class DocumentCategory_Fields:
    # Fields directly copied from DocumentCategory_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class DocumentTemplate_Fields:
    # Fields directly copied from DocumentTemplate_base
    id: Optional[int] = None
    etag: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None
    filename: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    document_category: Optional[DocumentCategory_base] = None
    last_modified_by: Optional[User_base] = None

@dataclass
class Folder_Fields:
    # Fields directly copied from Folder_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    root: Optional[bool] = None

    # Nested resource fields
    parent: Optional[LinkedFolder_base] = None
    matter: Optional[Matter_base] = None
    contact: Optional[Contact_base] = None
    document_category: Optional[DocumentCategory_base] = None
    creator: Optional[ClioCreator_base] = None
    latest_document_version: Optional[DocumentVersion_base] = None
    group: Optional[Group_base] = None
    external_properties: Optional[ExternalProperty_base] = None

@dataclass
class Item_Fields:
    # Fields directly copied from Item_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None

    # Nested resource fields
    parent: Optional[LinkedFolder_base] = None
    matter: Optional[Matter_base] = None
    contact: Optional[Contact_base] = None
    document_category: Optional[DocumentCategory_base] = None
    creator: Optional[ClioCreator_base] = None
    latest_document_version: Optional[DocumentVersion_base] = None
    group: Optional[Group_base] = None
    external_properties: Optional[ExternalProperty_base] = None

@dataclass
class Account_Fields:
    # Fields directly copied from Account_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    owner: Optional[User_base] = None

@dataclass
class ActivityDescription_Fields:
    # Fields directly copied from ActivityDescription_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    visible_to_co_counsel: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    default: Optional[bool] = None
    type: Optional[str] = None
    utbms_activity_id: Optional[int] = None
    utbms_task_name: Optional[str] = None
    utbms_task_id: Optional[int] = None
    xero_service_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    category_type: Optional[str] = None
    currency: Optional[dict] = None

    # Nested resource fields
    groups: Optional[Group_base] = None
    rate: Optional[ActivityDescriptionRate_base] = None
    utbms_task: Optional[UtbmsCode_base] = None
    utbms_activity: Optional[UtbmsCode_base] = None

@dataclass
class ActivityRate_Fields:
    # Fields directly copied from ActivityRate_base
    id: Optional[int] = None
    etag: Optional[str] = None
    rate: Optional[float] = None
    flat_rate: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    contact_id: Optional[int] = None
    co_counsel_contact_id: Optional[int] = None

    # Nested resource fields
    user: Optional[User_base] = None
    group: Optional[Group_base] = None

@dataclass
class Activity_Fields:
    # Fields directly copied from Activity_base
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    quantity_in_hours: Optional[float] = None
    rounded_quantity_in_hours: Optional[float] = None
    quantity: Optional[float] = None
    rounded_quantity: Optional[float] = None
    quantity_redacted: Optional[bool] = None
    price: Optional[float] = None
    note: Optional[str] = None
    flat_rate: Optional[bool] = None
    billed: Optional[bool] = None
    on_bill: Optional[bool] = None
    total: Optional[float] = None
    contingency_fee: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    reference: Optional[str] = None
    non_billable: Optional[bool] = None
    non_billable_total: Optional[float] = None
    no_charge: Optional[bool] = None
    tax_setting: Optional[str] = None
    currency: Optional[dict] = None

    # Nested resource fields
    activity_description: Optional[ActivityDescription_base] = None
    expense_category: Optional[ExpenseCategory_base] = None
    bill: Optional[Bill_base] = None
    communication: Optional[Communication_base] = None
    client_portal: Optional[ClientPortal_base] = None
    matter: Optional[Matter_base] = None
    matter_note: Optional[Note_base] = None
    contact_note: Optional[Note_base] = None
    subject: Optional[PolymorphicObject_base] = None
    timer: Optional[Timer_base] = None
    user: Optional[User_base] = None
    utbms_expense: Optional[UtbmsCode_base] = None
    vendor: Optional[Contact_base] = None
    calendar_entry: Optional[Activity_CalendarEntry_base] = None
    task: Optional[Activity_Task_base] = None
    text_message_conversation: Optional[Activity_TextMessageConversation_base] = None
    document_version: Optional[DocumentVersion_base] = None
    legal_aid_uk_activity: Optional[LegalAidUkActivity_base] = None
    currency: Optional[Currency_base] = None

@dataclass
class Address_Fields:
    # Fields directly copied from Address_base
    id: Optional[int] = None
    etag: Optional[str] = None
    street: Optional[str] = None
    city: Optional[str] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    primary: Optional[bool] = None

@dataclass
class Allocation_Fields:
    # Fields directly copied from Allocation_base
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    interest: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    description: Optional[str] = None
    has_online_payment: Optional[bool] = None
    destroyable: Optional[bool] = None
    payment_type: Optional[str] = None

    # Nested resource fields
    bill: Optional[Bill_base] = None
    source_bank_account: Optional[BankAccount_base] = None
    destination_bank_account: Optional[BankAccount_base] = None
    matter: Optional[Matter_base] = None
    contact: Optional[Contact_base] = None
    parent: Optional[PolymorphicObject_base] = None

@dataclass
class Balance_Fields:
    # Fields directly copied from Balance_base
    id: Optional[int] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    interest_amount: Optional[float] = None
    due: Optional[float] = None

@dataclass
class BankAccount_Fields:
    # Fields directly copied from BankAccount_base
    account_number: Optional[str] = None
    balance: Optional[float] = None
    bank_transactions_count: Optional[int] = None
    clio_payment_page_link: Optional[str] = None
    clio_payment_page_qr_code: Optional[str] = None
    clio_payments_enabled: Optional[bool] = None
    controlled_account: Optional[bool] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    currency_id: Optional[float] = None
    default_account: Optional[bool] = None
    domicile_branch: Optional[str] = None
    etag: Optional[str] = None
    general_ledger_number: Optional[str] = None
    holder: Optional[str] = None
    id: Optional[int] = None
    institution: Optional[str] = None
    name: Optional[str] = None
    swift: Optional[str] = None
    transit_number: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    user: Optional[User_base] = None

@dataclass
class BankTransaction_Fields:
    # Fields directly copied from BankTransaction_base
    id: Optional[int] = None
    type: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    bank_account_id: Optional[int] = None
    source: Optional[str] = None
    confirmation: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    exchange_rate: Optional[float] = None
    transaction_type: Optional[str] = None
    funds_in: Optional[float] = None
    funds_out: Optional[float] = None
    clio_payments_transaction: Optional[bool] = None
    current_account_balance: Optional[float] = None
    read_only_confirmation: Optional[bool] = None

    # Nested resource fields
    client: Optional[Contact_base] = None
    matter: Optional[Matter_base] = None
    bank_account: Optional[BankAccount_base] = None
    bill: Optional[Bill_base] = None
    allocation: Optional[Allocation_base] = None

@dataclass
class BankTransfer_Fields:
    # Fields directly copied from BankTransfer_base
    id: Optional[int] = None
    etag: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    description: Optional[str] = None
    primary_authorizer: Optional[str] = None
    secondary_authorizer: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    client: Optional[Contact_base] = None
    destination_account: Optional[BankAccount_base] = None
    matter: Optional[Matter_base] = None
    source_account: Optional[BankAccount_base] = None

@dataclass
class Bill_Fields:
    # Fields directly copied from Bill_base
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    issued_at: Optional[str] = None
    created_at: Optional[str] = None
    due_at: Optional[str] = None
    tax_rate: Optional[float] = None
    secondary_tax_rate: Optional[float] = None
    updated_at: Optional[str] = None
    subject: Optional[str] = None
    purchase_order: Optional[str] = None
    type: Optional[str] = None
    memo: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    balance: Optional[float] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    total: Optional[float] = None
    paid: Optional[float] = None
    paid_at: Optional[str] = None
    pending: Optional[float] = None
    due: Optional[float] = None
    discount_services_only: Optional[str] = None
    can_update: Optional[bool] = None
    credits_issued: Optional[float] = None
    shared: Optional[bool] = None
    last_sent_at: Optional[str] = None
    services_secondary_tax: Optional[float] = None
    services_sub_total: Optional[float] = None
    services_tax: Optional[float] = None
    services_taxable_sub_total: Optional[int] = None
    services_secondary_taxable_sub_total: Optional[int] = None
    taxable_sub_total: Optional[int] = None
    secondary_taxable_sub_total: Optional[int] = None
    sub_total: Optional[float] = None
    tax_sum: Optional[float] = None
    secondary_tax_sum: Optional[float] = None
    total_tax: Optional[float] = None
    available_state_transitions: Optional[List[str]] = None

    # Nested resource fields
    user: Optional[User_base] = None
    client: Optional[Contact_base] = None
    discount: Optional[Discount_base] = None
    interest: Optional[Interest_base] = None
    matters: Optional[Matter_base] = None
    group: Optional[Group_base] = None
    bill_theme: Optional[BillTheme_base] = None
    original_bill: Optional[Bill_base] = None
    destination_account: Optional[BankAccount_base] = None
    balances: Optional[Balance_base] = None
    matter_totals: Optional[MatterBalance_base] = None
    currency: Optional[Currency_base] = None
    billing_setting: Optional[BillingSetting_base] = None
    client_addresses: Optional[Address_base] = None
    legal_aid_uk_bill: Optional[LegalAidUkBill_base] = None

@dataclass
class BillTheme_Fields:
    # Fields directly copied from BillTheme_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    account_id: Optional[int] = None
    default: Optional[bool] = None
    name: Optional[str] = None
    config: Optional[str] = None

@dataclass
class BillableClient_Fields:
    # Fields directly copied from BillableClient_base
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    name: Optional[str] = None
    billable_matters_count: Optional[int] = None

    # Nested resource fields
    billable_matters: Optional[BillableMatter_base] = None

@dataclass
class BillableMatter_Fields:
    # Fields directly copied from BillableMatter_base
    currency_code: Optional[str] = None
    currency_id: Optional[int] = None
    id: Optional[int] = None
    unbilled_hours: Optional[float] = None
    unbilled_amount: Optional[float] = None
    amount_in_trust: Optional[float] = None
    display_number: Optional[str] = None

    # Nested resource fields
    client: Optional[Contact_base] = None

@dataclass
class CalendarEntryEventType_Fields:
    # Fields directly copied from CalendarEntryEventType_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    color: Optional[str] = None
    name: Optional[str] = None

@dataclass
class CalendarEntry_Fields:
    # Fields directly copied from CalendarEntry_base
    id: Optional[str] = None
    etag: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    all_day: Optional[bool] = None
    recurrence_rule: Optional[str] = None
    parent_calendar_entry_id: Optional[int] = None
    court_rule: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    permission: Optional[str] = None
    calendar_owner_id: Optional[int] = None
    start_at_time_zone: Optional[str] = None
    time_entries_count: Optional[int] = None

    # Nested resource fields
    time_entries: Optional[Activity_base] = None
    conference_meeting: Optional[ConferenceMeeting_base] = None
    matter: Optional[Matter_base] = None
    matter_docket: Optional[MatterDocket_base] = None
    calendar_owner: Optional[Calendar_base] = None
    parent_calendar_entry: Optional[CalendarEntry_base] = None
    calendar_entry_event_type: Optional[CalendarEntryEventType_base] = None
    attendees: Optional[Attendee_base] = None
    calendars: Optional[Calendar_base] = None
    reminders: Optional[Reminder_base] = None
    external_properties: Optional[ExternalProperty_base] = None

@dataclass
class Calendar_Fields:
    # Fields directly copied from Calendar_base
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    court_rules_default_calendar: Optional[bool] = None
    name: Optional[str] = None
    permission: Optional[str] = None
    type: Optional[str] = None
    visible: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    source: Optional[str] = None

    # Nested resource fields
    creator: Optional[User_base] = None

@dataclass
class ClioPaymentsLink_Fields:
    # Fields directly copied from ClioPaymentsLink_base
    active: Optional[bool] = None
    amount: Optional[float] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    etag: Optional[str] = None
    expires_at: Optional[str] = None
    id: Optional[int] = None
    is_allocated_as_revenue: Optional[bool] = None
    redirect_url: Optional[str] = None
    url: Optional[str] = None

    # Nested resource fields
    bank_account: Optional[BankAccount_base] = None
    bill: Optional[Bill_base] = None
    clio_payments_payment: Optional[ClioPaymentsPayment_base] = None
    contact: Optional[Contact_base] = None
    destination_account: Optional[BankAccount_base] = None
    destination_contact: Optional[Contact_base] = None

@dataclass
class ClioPaymentsPayment_Fields:
    # Fields directly copied from ClioPaymentsPayment_base
    amount: Optional[float] = None
    confirmation_number: Optional[str] = None
    created_at: Optional[str] = None
    currency: Optional[str] = None
    deposit_as_revenue: Optional[bool] = None
    description: Optional[str] = None
    email_address: Optional[str] = None
    id: Optional[int] = None
    state: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    bank_transaction: Optional[BankTransaction_base] = None
    clio_payments_link: Optional[ClioPaymentsLink_base] = None
    contact: Optional[Contact_base] = None
    destination_account: Optional[BankAccount_base] = None
    user: Optional[User_base] = None
    allocations: Optional[Allocation_base] = None
    bills: Optional[Bill_base] = None
    matters: Optional[Matter_base] = None

@dataclass
class ConversationMessage_Fields:
    # Fields directly copied from ConversationMessage_base
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    body: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    sender: Optional[UnredactedParticipant_base] = None
    document: Optional[Document_base] = None
    conversation: Optional[Conversation_base] = None
    receivers: Optional[UnredactedParticipant_base] = None

@dataclass
class Jurisdiction_Fields:
    # Fields directly copied from Jurisdiction_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None
    display_timezone: Optional[str] = None
    valid_subscription: Optional[bool] = None
    is_local_timezone: Optional[bool] = None

    # Nested resource fields
    service_types: Optional[ServiceType_base] = None

@dataclass
class JurisdictionsToTrigger_Fields:
    # Fields directly copied from JurisdictionsToTrigger_base
    id: Optional[int] = None
    etag: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    do_not_recalculate: Optional[bool] = None
    is_served: Optional[bool] = None
    is_requirements_required: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class MatterDocket_Fields:
    # Fields directly copied from MatterDocket_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    start_date: Optional[str] = None
    start_time: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None
    jurisdiction: Optional[Jurisdiction_base] = None
    trigger: Optional[JurisdictionsToTrigger_base] = None
    service_type: Optional[ServiceType_base] = None
    calendar_entries: Optional[CalendarEntry_base] = None

@dataclass
class ServiceType_Fields:
    # Fields directly copied from ServiceType_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    system_id: Optional[int] = None
    description: Optional[str] = None
    default: Optional[bool] = None

@dataclass
class CreditMemo_Fields:
    # Fields directly copied from CreditMemo_base
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    discount: Optional[bool] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    user: Optional[User_base] = None
    contact: Optional[Contact_base] = None
    allocations: Optional[Allocation_base] = None

@dataclass
class Currency_Fields:
    # Fields directly copied from Currency_base
    id: Optional[int] = None
    etag: Optional[str] = None
    code: Optional[str] = None
    sign: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class CustomAction_Fields:
    # Fields directly copied from CustomAction_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    label: Optional[str] = None
    target_url: Optional[str] = None
    ui_reference: Optional[str] = None

@dataclass
class CustomField_Fields:
    # Fields directly copied from CustomField_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    field_type: Optional[str] = None
    displayed: Optional[bool] = None
    deleted: Optional[bool] = None
    required: Optional[bool] = None
    display_order: Optional[int] = None

    # Nested resource fields
    picklist_options: Optional[PicklistOption_base] = None

@dataclass
class CustomFieldSet_Fields:
    # Fields directly copied from CustomFieldSet_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    parent_type: Optional[str] = None
    displayed: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    custom_fields: Optional[CustomField_base] = None

@dataclass
class EmailAddress_Fields:
    # Fields directly copied from EmailAddress_base
    id: Optional[int] = None
    etag: Optional[str] = None
    address: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class ExpenseCategory_Fields:
    # Fields directly copied from ExpenseCategory_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[int] = None
    entry_type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    xero_expense_code: Optional[str] = None
    accessible_to_user: Optional[bool] = None
    tax_setting: Optional[str] = None
    currency: Optional[dict] = None

    # Nested resource fields
    groups: Optional[Group_base] = None
    utbms_code: Optional[UtbmsCode_base] = None

@dataclass
class GrantFundingSource_Fields:
    # Fields directly copied from GrantFundingSource_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    grants: Optional[Grant_base] = None

@dataclass
class Grant_Fields:
    # Fields directly copied from Grant_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    funding_code: Optional[str] = None
    funding_code_and_name: Optional[str] = None
    funding_source_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    balance: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    # Nested resource fields
    grant_funding_source: Optional[GrantFundingSource_base] = None

@dataclass
class Group_Fields:
    # Fields directly copied from Group_base
    client_connect_user: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    users: Optional[User_base] = None

@dataclass
class InterestCharge_Fields:
    # Fields directly copied from InterestCharge_base
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    description: Optional[str] = None
    total: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    bill: Optional[Bill_base] = None
    balances: Optional[Balance_base] = None
    matters: Optional[Matter_base] = None

@dataclass
class Interest_Fields:
    # Fields directly copied from Interest_base
    balance: Optional[float] = None
    period: Optional[int] = None
    rate: Optional[float] = None
    total: Optional[float] = None
    type: Optional[str] = None

@dataclass
class EventMetrics_Fields:
    # Fields directly copied from EventMetrics_base
    unread_mobile_events: Optional[int] = None
    unread_web_events: Optional[int] = None
    unread_secure_messages: Optional[int] = None
    unread_client_portal_messages: Optional[int] = None
    unread_text_messages: Optional[int] = None

@dataclass
class MyEvent_Fields:
    # Fields directly copied from MyEvent_base

    # Nested resource fields
    event: Optional[Event_base] = None

@dataclass
class Event_Fields:
    # Fields directly copied from Event_base
    id: Optional[int] = None
    etag: Optional[str] = None
    message: Optional[str] = None
    icon: Optional[str] = None
    title: Optional[str] = None
    title_url: Optional[str] = None
    description: Optional[str] = None
    description_url: Optional[str] = None
    primary_detail: Optional[str] = None
    primary_detail_url: Optional[str] = None
    secondary_detail: Optional[str] = None
    secondary_detail_url: Optional[str] = None
    occurred_at: Optional[str] = None
    mobile_icon: Optional[str] = None
    subject_type: Optional[str] = None
    subject_id: Optional[int] = None

@dataclass
class LaukCivilCertificatedRate_Fields:
    # Fields directly copied from LaukCivilCertificatedRate_base
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_sub_category: Optional[str] = None
    activity_type: Optional[str] = None
    attended_several_hearings_for_multiple_clients: Optional[bool] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    change_of_solicitor: Optional[bool] = None
    court: Optional[str] = None
    eligible_for_sqm: Optional[bool] = None
    exceptional: Optional[float] = None
    exceptional_warning: Optional[str] = None
    etag: Optional[str] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    first_conducting_solicitor: Optional[bool] = None
    key: Optional[str] = None
    number_of_clients: Optional[str] = None
    party: Optional[str] = None
    post_transfer_clients_represented: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    session_type: Optional[str] = None
    user_type: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class LaukCivilControlledRate_Fields:
    # Fields directly copied from LaukCivilControlledRate_base
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class LaukCriminalControlledRate_Fields:
    # Fields directly copied from LaukCriminalControlledRate_base
    id: Optional[int] = None
    activity: Optional[str] = None
    activity_type: Optional[str] = None
    category_of_law: Optional[str] = None
    counsel: Optional[str] = None
    court: Optional[str] = None
    created_at: Optional[str] = None
    etag: Optional[str] = None
    exceptional: Optional[float] = None
    fee: Optional[float] = None
    fee_scheme: Optional[str] = None
    post_nov_24_exceptional: Optional[float] = None
    post_nov_24_fee: Optional[float] = None
    post_sept_22_exceptional: Optional[float] = None
    post_sept_22_fee: Optional[float] = None
    key: Optional[str] = None
    rate_type: Optional[str] = None
    region: Optional[str] = None
    solicitor_type: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class LaukExpenseCategory_Fields:
    # Fields directly copied from LaukExpenseCategory_base
    certificated: Optional[bool] = None
    civil: Optional[bool] = None
    created_at: Optional[str] = None
    criminal: Optional[bool] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    rate: Optional[float] = None
    updated_at: Optional[str] = None

@dataclass
class LineItem_Fields:
    # Fields directly copied from LineItem_base
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = None
    price: Optional[float] = None
    taxable: Optional[bool] = None
    kind: Optional[str] = None
    note: Optional[str] = None
    secondary_taxable: Optional[bool] = None
    total: Optional[float] = None
    tax: Optional[float] = None
    secondary_tax: Optional[float] = None
    sub_total: Optional[float] = None
    quantity: Optional[float] = None
    group_ordering: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    bill: Optional[Bill_base] = None
    activity: Optional[Activity_base] = None
    matter: Optional[Matter_base] = None
    user: Optional[User_base] = None
    discount: Optional[Discount_base] = None
    included_line_item_totals: Optional[LineItemTotals_base] = None

@dataclass
class LogEntry_Fields:
    # Fields directly copied from LogEntry_base
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    accessed_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    item: Optional[PolymorphicObject_base] = None
    user: Optional[User_base] = None

@dataclass
class MatterStage_Fields:
    # Fields directly copied from MatterStage_base
    id: Optional[int] = None
    etag: Optional[str] = None
    practice_area_id: Optional[str] = None
    name: Optional[str] = None
    order: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class Client_Fields:
    # Fields directly copied from Client_base
    id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[int] = None
    date_of_birth: Optional[str] = None

    # Nested resource fields
    avatar: Optional[Avatar_base] = None
    company: Optional[Contact_base] = None
    addresses: Optional[Address_base] = None
    email_addresses: Optional[EmailAddress_base] = None
    phone_numbers: Optional[PhoneNumber_base] = None
    web_sites: Optional[WebSite_base] = None

@dataclass
class MatterContacts_Fields:
    # Fields directly copied from MatterContacts_base
    contact_created_at: Optional[str] = None
    contact_updated_at: Optional[str] = None
    created_at: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    is_client: Optional[bool] = None
    last_name: Optional[str] = None
    matter_id: Optional[int] = None
    matter_number: Optional[str] = None
    middle_name: Optional[str] = None
    name: Optional[str] = None
    prefix: Optional[str] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    relationship_name: Optional[str] = None
    secondary_email_address: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updated_at: Optional[str] = None
    client_connect_user_id: Optional[int] = None

    # Nested resource fields
    avatar: Optional[Avatar_base] = None
    company: Optional[Contact_base] = None
    primary_address: Optional[Address_base] = None
    primary_web_site: Optional[WebSite_base] = None
    secondary_address: Optional[Address_base] = None
    secondary_web_site: Optional[WebSite_base] = None
    addresses: Optional[Address_base] = None
    custom_field_values: Optional[CustomFieldValue_base] = None
    email_addresses: Optional[EmailAddress_base] = None
    phone_numbers: Optional[PhoneNumber_base] = None
    web_sites: Optional[WebSite_base] = None
    relationship: Optional[Relationship_base] = None

@dataclass
class RelatedContacts_Fields:
    # Fields directly copied from RelatedContacts_base
    id: Optional[int] = None
    contact_id: Optional[int] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    is_matter_client: Optional[bool] = None
    primary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    client_connect_user_id: Optional[int] = None

    # Nested resource fields
    avatar: Optional[Avatar_base] = None
    company: Optional[Contact_base] = None
    primary_address: Optional[Address_base] = None
    primary_web_site: Optional[WebSite_base] = None
    secondary_address: Optional[Address_base] = None
    secondary_web_site: Optional[WebSite_base] = None
    addresses: Optional[Address_base] = None
    custom_field_values: Optional[CustomFieldValue_base] = None
    email_addresses: Optional[EmailAddress_base] = None
    phone_numbers: Optional[PhoneNumber_base] = None
    web_sites: Optional[WebSite_base] = None
    relationship: Optional[Relationship_base] = None

@dataclass
class Note_Fields:
    # Fields directly copied from Note_base
    id: Optional[int] = None
    etag: Optional[str] = None
    type: Optional[str] = None
    subject: Optional[str] = None
    detail: Optional[str] = None
    date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None
    contact: Optional[Contact_base] = None
    author: Optional[User_base] = None
    time_entries: Optional[Activity_base] = None
    notification_event_subscribers: Optional[NotificationEventSubscriber_base] = None

@dataclass
class OutstandingClientBalance_Fields:
    # Fields directly copied from OutstandingClientBalance_base
    associated_matter_ids: Optional[List[int]] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    last_payment_date: Optional[str] = None
    last_shared_date: Optional[str] = None
    newest_issued_bill_due_date: Optional[str] = None
    pending_payments_total: Optional[float] = None
    reminders_enabled: Optional[bool] = None
    total_outstanding_balance: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    outstanding_bills: Optional[Bill_base] = None
    contact: Optional[Contact_base] = None
    currency: Optional[Currency_base] = None

@dataclass
class Payment_Fields:
    # Fields directly copied from Payment_base
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    reference: Optional[str] = None
    amount: Optional[float] = None
    date: Optional[str] = None
    source_fund_type: Optional[str] = None
    voided_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    contact: Optional[Contact_base] = None
    user: Optional[User_base] = None
    source_bank_account: Optional[BankAccount_base] = None
    destination_bank_account: Optional[BankAccount_base] = None
    allocations: Optional[Allocation_base] = None

@dataclass
class Damage_Fields:
    # Fields directly copied from Damage_base
    id: Optional[int] = None
    amount: Optional[float] = None
    damage_type: Optional[str] = None
    description: Optional[str] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None

@dataclass
class MedicalBill_Fields:
    # Fields directly copied from MedicalBill_base
    id: Optional[int] = None
    adjustment: Optional[float] = None
    amount: Optional[float] = None
    bill_date: Optional[str] = None
    bill_received_date: Optional[str] = None
    damage_type: Optional[str] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None
    liens: Optional[Lien_base] = None

@dataclass
class MedicalRecord_Fields:
    # Fields directly copied from MedicalRecord_base
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    end_date: Optional[str] = None
    start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None

@dataclass
class MedicalRecordsRequest_Fields:
    # Fields directly copied from MedicalRecordsRequest_base
    id: Optional[int] = None
    etag: Optional[str] = None
    bills_follow_up_date: Optional[str] = None
    bills_request_date: Optional[str] = None
    bills_status: Optional[str] = None
    description: Optional[str] = None
    in_treatment: Optional[bool] = None
    records_follow_up_date: Optional[str] = None
    records_request_date: Optional[str] = None
    records_status: Optional[str] = None
    treatment_end_date: Optional[str] = None
    treatment_start_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None
    medical_provider: Optional[Contact_base] = None
    medical_bills: Optional[MedicalBill_base] = None
    medical_records: Optional[MedicalRecord_base] = None

@dataclass
class PhoneNumber_Fields:
    # Fields directly copied from PhoneNumber_base
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[str] = None
    name: Optional[str] = None
    primary: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class PracticeArea_Fields:
    # Fields directly copied from PracticeArea_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    name: Optional[str] = None
    category: Optional[str] = None
    code: Optional[str] = None

@dataclass
class Relationship_Fields:
    # Fields directly copied from Relationship_base
    id: Optional[int] = None
    etag: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    matter: Optional[Matter_base] = None
    contact: Optional[Contact_base] = None

@dataclass
class Reminder_Fields:
    # Fields directly copied from Reminder_base
    id: Optional[int] = None
    etag: Optional[str] = None
    duration: Optional[int] = None
    next_delivery_at: Optional[str] = None
    state: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    notification_method: Optional[NotificationMethod_base] = None
    subject: Optional[PolymorphicObject_base] = None

@dataclass
class ReportPreset_Fields:
    # Fields directly copied from ReportPreset_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    last_generated_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    options: Optional[str] = None

    # Nested resource fields
    report_schedule: Optional[ReportSchedule_base] = None

@dataclass
class ReportSchedule_Fields:
    # Fields directly copied from ReportSchedule_base
    id: Optional[int] = None
    etag: Optional[str] = None
    time_of_day: Optional[str] = None
    frequency: Optional[str] = None
    days_of_week: Optional[List[int]] = None
    day_of_month: Optional[int] = None
    status: Optional[str] = None
    status_updated_at: Optional[str] = None
    next_scheduled_date: Optional[str] = None
    time_zone: Optional[str] = None
    report_preset_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    every_no_of_months: Optional[int] = None
    effective_from: Optional[str] = None

@dataclass
class Report_Fields:
    # Fields directly copied from Report_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    state: Optional[str] = None
    kind: Optional[str] = None
    format: Optional[str] = None
    progress: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

@dataclass
class BillingSetting_Fields:
    # Fields directly copied from BillingSetting_base
    id: Optional[int] = None
    etag: Optional[str] = None
    rounded_duration: Optional[float] = None
    rounding: Optional[int] = None
    use_decimal_rounding: Optional[bool] = None
    currency: Optional[str] = None
    currency_sign: Optional[str] = None
    tax_rate: Optional[float] = None
    tax_name: Optional[str] = None
    apply_tax_by_default: Optional[bool] = None
    time_on_flat_rate_contingency_matters_is_non_billable: Optional[bool] = None
    use_secondary_tax: Optional[bool] = None
    secondary_tax_rate: Optional[float] = None
    secondary_tax_rule: Optional[str] = None
    secondary_tax_name: Optional[str] = None
    notify_after_bill_created: Optional[bool] = None
    use_utbms_codes: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class TextSnippet_Fields:
    # Fields directly copied from TextSnippet_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    snippet: Optional[str] = None
    phrase: Optional[str] = None
    whole_word: Optional[bool] = None

@dataclass
class CalendarVisibility_Fields:
    # Fields directly copied from CalendarVisibility_base
    id: Optional[int] = None
    etag: Optional[str] = None
    color: Optional[str] = None
    light_color: Optional[str] = None
    visible: Optional[bool] = None
    name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class TaskTemplateList_Fields:
    # Fields directly copied from TaskTemplateList_base
    created_at: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    templates_count: Optional[int] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    practice_area: Optional[PracticeArea_base] = None
    creator: Optional[User_base] = None

@dataclass
class TaskTemplate_Fields:
    # Fields directly copied from TaskTemplate_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    private: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    cascading_source: Optional[CascadingTaskTemplate_base] = None
    assignee: Optional[User_base] = None
    task_template_list: Optional[TaskTemplateList_base] = None
    task_type: Optional[TaskType_base] = None
    template_creator: Optional[User_base] = None
    reminder_templates: Optional[ReminderTemplate_base] = None

@dataclass
class TaskType_Fields:
    # Fields directly copied from TaskType_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    deleted_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class Timer_Fields:
    # Fields directly copied from Timer_base
    id: Optional[int] = None
    etag: Optional[str] = None
    start_time: Optional[str] = None
    elapsed_time: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    activity: Optional[Activity_base] = None

@dataclass
class TrustLineItem_Fields:
    # Fields directly copied from TrustLineItem_base
    id: Optional[int] = None
    etag: Optional[str] = None
    date: Optional[str] = None
    total: Optional[float] = None
    note: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    bill: Optional[Bill_base] = None
    matter: Optional[Matter_base] = None
    client: Optional[Contact_base] = None

@dataclass
class TrustRequest_Fields:
    # Fields directly copied from TrustRequest_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class User_Fields:
    # Fields directly copied from User_base
    account_owner: Optional[bool] = None
    clio_connect: Optional[bool] = None
    court_rules_default_attendee: Optional[bool] = None
    created_at: Optional[str] = None
    default_calendar_id: Optional[int] = None
    email: Optional[str] = None
    enabled: Optional[bool] = None
    etag: Optional[str] = None
    first_name: Optional[str] = None
    id: Optional[int] = None
    initials: Optional[str] = None
    last_name: Optional[str] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    rate: Optional[float] = None
    roles: Optional[List[str]] = None
    subscription_type: Optional[str] = None
    time_zone: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    default_activity_description: Optional[ActivityDescription_base] = None
    notification_methods: Optional[NotificationMethod_base] = None
    account: Optional[Account_base] = None
    avatar: Optional[Avatar_base] = None
    contact: Optional[Contact_base] = None
    job_title: Optional[JobTitle_base] = None
    groups: Optional[Group_base] = None

@dataclass
class UtbmsCode_Fields:
    # Fields directly copied from UtbmsCode_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    utbms_set_id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class UtbmsSet_Fields:
    # Fields directly copied from UtbmsSet_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    enabled: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

@dataclass
class Webhook_Fields:
    # Fields directly copied from Webhook_base
    id: Optional[int] = None
    etag: Optional[str] = None
    url: Optional[str] = None
    fields: Optional[str] = None
    shared_secret: Optional[str] = None
    model: Optional[str] = None
    status: Optional[str] = None
    events: Optional[List[str]] = None
    expires_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    user: Optional[User_base] = None

@dataclass
class Multipart_Fields:
    # Fields directly copied from Multipart_base
    part_number: Optional[int] = None
    put_url: Optional[str] = None

    # Nested resource fields
    put_headers: Optional[MultipartHeader_base] = None

@dataclass
class BillRecipient_Fields:
    # Fields directly copied from BillRecipient_base
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    on_all_matters: Optional[bool] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    recipient: Optional[BillRecipient_Contact_base] = None

@dataclass
class ConversationMembership_Fields:
    # Fields directly copied from ConversationMembership_base
    id: Optional[int] = None
    etag: Optional[str] = None
    read: Optional[bool] = None
    archived: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    member: Optional[UnredactedParticipant_base] = None

@dataclass
class MatterBillRecipient_Fields:
    # Fields directly copied from MatterBillRecipient_base
    created_at: Optional[str] = None
    etag: Optional[str] = None
    id: Optional[int] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    recipient: Optional[Contact_base] = None

@dataclass
class Participant_Fields:
    # Fields directly copied from Participant_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    type: Optional[str] = None
    identifier: Optional[str] = None
    secondary_identifier: Optional[str] = None
    enabled: Optional[bool] = None
    name: Optional[str] = None
    initials: Optional[str] = None
    job_title_name: Optional[str] = None

    # Nested resource fields
    avatar: Optional[Avatar_base] = None

@dataclass
class CustomFieldMatterSelection_Fields:
    # Fields directly copied from CustomFieldMatterSelection_base
    id: Optional[int] = None
    display_number: Optional[str] = None

@dataclass
class PicklistOption_Fields:
    # Fields directly copied from PicklistOption_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    option: Optional[str] = None
    deleted_at: Optional[str] = None

@dataclass
class PolymorphicCustomRate_Fields:
    # Fields directly copied from PolymorphicCustomRate_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    rate: Optional[float] = None
    award: Optional[float] = None
    note: Optional[str] = None
    date: Optional[str] = None

    # Nested resource fields
    user: Optional[PolymorphicCustomRate_User_base] = None
    group: Optional[PolymorphicCustomRate_Group_base] = None
    activity_description: Optional[PolymorphicCustomRate_ActivityDescription_base] = None

@dataclass
class DocumentVersion_Fields:
    # Fields directly copied from DocumentVersion_base
    id: Optional[int] = None
    document_id: Optional[int] = None
    etag: Optional[str] = None
    uuid: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    version_number: Optional[int] = None
    content_type: Optional[str] = None
    received_at: Optional[str] = None
    put_url: Optional[str] = None
    fully_uploaded: Optional[bool] = None

    # Nested resource fields
    creator: Optional[ClioCreator_base] = None
    put_headers: Optional[MultipartHeader_base] = None
    multiparts: Optional[Multipart_Fields] = None

@dataclass
class Communication_Fields:
    # Fields directly copied from Communication_base
    id: Optional[int] = None
    etag: Optional[str] = None
    subject: Optional[str] = None
    body: Optional[str] = None
    type: Optional[str] = None
    date: Optional[str] = None
    time_entries_count: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    received_at: Optional[str] = None

    # Nested resource fields
    user: Optional[User_base] = None
    matter: Optional[Matter_base] = None
    communication_eml_file: Optional[CommunicationEmlFile_base] = None
    senders: Optional[Participant_Fields] = None
    receivers: Optional[Participant_Fields] = None
    external_properties: Optional[ExternalProperty_base] = None
    time_entries: Optional[Activity_base] = None
    documents: Optional[Document_base] = None
    notification_event_subscribers: Optional[NotificationEventSubscriber_base] = None

@dataclass
class Conversation_Fields:
    # Fields directly copied from Conversation_base
    id: Optional[int] = None
    etag: Optional[str] = None
    archived: Optional[bool] = None
    read_only: Optional[bool] = None
    current_user_is_member: Optional[bool] = None
    subject: Optional[str] = None
    message_count: Optional[int] = None
    time_entries_count: Optional[int] = None
    read: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    # Nested resource fields
    last_message: Optional[ConversationMessage_base] = None
    first_message: Optional[ConversationMessage_base] = None
    matter: Optional[Matter_base] = None
    messages: Optional[ConversationMessage_base] = None
    documents: Optional[Document_base] = None
    memberships: Optional[ConversationMembership_Fields] = None

@dataclass
class Task_Fields:
    # Fields directly copied from Task_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    status: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[str] = None
    due_at: Optional[str] = None
    permission: Optional[str] = None
    completed_at: Optional[str] = None
    notify_completion: Optional[bool] = None
    statute_of_limitations: Optional[bool] = None
    time_estimated: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    time_entries_count: Optional[int] = None

    # Nested resource fields
    time_entries: Optional[Activity_base] = None
    task_type: Optional[TaskType_base] = None
    assigner: Optional[User_base] = None
    matter: Optional[Matter_base] = None
    assignee: Optional[Participant_Fields] = None
    reminders: Optional[Reminder_base] = None

@dataclass
class CustomFieldValue_Fields:
    # Fields directly copied from CustomFieldValue_base
    id: Optional[str] = None
    etag: Optional[str] = None
    field_name: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    field_type: Optional[str] = None
    field_required: Optional[bool] = None
    field_displayed: Optional[bool] = None
    field_display_order: Optional[int] = None
    value: Optional[str] = None
    soft_deleted: Optional[bool] = None

    # Nested resource fields
    custom_field: Optional[CustomField_Fields] = None
    picklist_option: Optional[PicklistOption_Fields] = None
    matter: Optional[CustomFieldMatterSelection_base] = None
    contact: Optional[Contact_base] = None

@dataclass
class MatterCustomRate_Fields:
    # Fields directly copied from MatterCustomRate_base
    type: Optional[str] = None
    on_invoice: Optional[bool] = None

    # Nested resource fields
    rates: Optional[PolymorphicCustomRate_Fields] = None

@dataclass
class Document_Fields:
    # Fields directly copied from Document_base
    id: Optional[int] = None
    etag: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    type: Optional[str] = None
    locked: Optional[bool] = None
    name: Optional[str] = None
    received_at: Optional[str] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    content_type: Optional[str] = None

    # Nested resource fields
    parent: Optional[LinkedFolder_base] = None
    matter: Optional[Matter_base] = None
    contact: Optional[Contact_base] = None
    document_category: Optional[DocumentCategory_base] = None
    creator: Optional[ClioCreator_base] = None
    latest_document_version: Optional[DocumentVersion_Fields] = None
    group: Optional[Group_base] = None
    external_properties: Optional[ExternalProperty_base] = None
    document_versions: Optional[DocumentVersion_base] = None

@dataclass
class Contact_Fields:
    # Fields directly copied from Contact_base
    id: Optional[int] = None
    etag: Optional[str] = None
    name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    type: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    prefix: Optional[str] = None
    title: Optional[str] = None
    initials: Optional[str] = None
    clio_connect_email: Optional[str] = None
    locked_clio_connect_email: Optional[bool] = None
    client_connect_user_id: Optional[int] = None
    primary_email_address: Optional[str] = None
    secondary_email_address: Optional[str] = None
    primary_phone_number: Optional[str] = None
    secondary_phone_number: Optional[str] = None
    ledes_client_id: Optional[str] = None
    has_clio_for_clients_permission: Optional[bool] = None
    is_client: Optional[bool] = None
    is_clio_for_client_user: Optional[bool] = None
    is_co_counsel: Optional[bool] = None
    is_bill_recipient: Optional[bool] = None
    sales_tax_number: Optional[str] = None
    currency: Optional[dict] = None

    # Nested resource fields
    activity_rates: Optional[ActivityRate_base] = None
    addresses: Optional[Address_base] = None
    custom_field_values: Optional[CustomFieldValue_Fields] = None
    custom_field_set_associations: Optional[CustomFieldSetAssociation_base] = None
    email_addresses: Optional[EmailAddress_base] = None
    instant_messengers: Optional[InstantMessenger_base] = None
    phone_numbers: Optional[PhoneNumber_base] = None
    web_sites: Optional[WebSite_base] = None
    notification_methods: Optional[NotificationMethod_base] = None
    account_balances: Optional[AccountBalance_base] = None
    related_contacts: Optional[Contact_base] = None
    primary_work_address: Optional[Address_base] = None
    primary_address: Optional[Address_base] = None
    secondary_address: Optional[Address_base] = None
    company: Optional[Contact_base] = None
    avatar: Optional[Avatar_base] = None
    payment_profile: Optional[PaymentProfile_base] = None
    folder: Optional[Folder_base] = None
    co_counsel_rate: Optional[ActivityRate_base] = None
    primary_web_site: Optional[WebSite_base] = None
    legal_aid_uk_contact: Optional[LegalAidUkContact_base] = None

@dataclass
class Matter_Fields:
    # Fields directly copied from Matter_base
    id: Optional[int] = None
    etag: Optional[str] = None
    number: Optional[int] = None
    display_number: Optional[str] = None
    custom_number: Optional[str] = None
    currency: Optional[dict] = None
    description: Optional[str] = None
    status: Optional[str] = None
    location: Optional[str] = None
    client_reference: Optional[str] = None
    client_id: Optional[int] = None
    billable: Optional[bool] = None
    maildrop_address: Optional[str] = None
    billing_method: Optional[str] = None
    open_date: Optional[str] = None
    close_date: Optional[str] = None
    pending_date: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    shared: Optional[bool] = None
    has_tasks: Optional[bool] = None
    last_activity_date: Optional[str] = None
    matter_stage_updated_at: Optional[str] = None

    # Nested resource fields
    client: Optional[Contact_base] = None
    contingency_fee: Optional[ContingencyFee_base] = None
    custom_rate: Optional[MatterCustomRate_Fields] = None
    evergreen_retainer: Optional[EvergreenRetainer_base] = None
    folder: Optional[Folder_base] = None
    group: Optional[Group_base] = None
    matter_budget: Optional[MatterBudget_base] = None
    matter_stage: Optional[MatterStage_base] = None
    originating_attorney: Optional[User_base] = None
    practice_area: Optional[PracticeArea_base] = None
    responsible_attorney: Optional[User_base] = None
    statute_of_limitations: Optional[Task_base] = None
    user: Optional[User_base] = None
    legal_aid_uk_matter: Optional[LegalAidUkMatter_base] = None
    account_balances: Optional[AccountBalance_base] = None
    custom_field_values: Optional[CustomFieldValue_Fields] = None
    custom_field_set_associations: Optional[CustomFieldSetAssociation_base] = None
    matter_bill_recipients: Optional[MatterBillRecipient_Fields] = None
    relationships: Optional[Relationship_base] = None
    task_template_list_instances: Optional[TaskTemplateListInstace_base] = None

