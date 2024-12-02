from dataclasses import dataclass
from datetime import date
from enum import Enum

@dataclass
class CreditTransaction:
    customer_number: str
    account_currency: str
    account_number: str
    account_type: str
    transaction_date: date
    transaction_posted_date: date
    amount: float
    type: str
    description: str
    fitid: str

@dataclass
class DebitTransaction:
    customer_number: str
    account_currency: str
    routing_number: str
    account_number: str
    account_type: str
    transaction_posted_date: date
    transaction_posted_time: str
    amount: float
    type: str
    description: str
    fitid: str

class DebitTransactionType(str, Enum):
    WITHDRAWAL = "Withdrawal"
    DEPOSIT = "Deposit"

class CreditTransactionType(str, Enum):
    PURCHASE = "Purchase"
    CASH_ADVANCE = "Cash Advance"
    FEE = "Fee"
    INTEREST = "Interest"
    OTHER = "Other"

class FileType(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"
