from credit import get_all_time_credit_spending
from debit import get_all_time_debit_spending
from schema import CreditTransaction, DebitTransaction


def get_all_time_spending(credit_transactions: list[CreditTransaction], debit_transactions: list[DebitTransaction]) -> float:
    total_spending = 0
    total_spending += get_all_time_credit_spending(credit_transactions)
    total_spending += get_all_time_debit_spending(debit_transactions)
    return total_spending


