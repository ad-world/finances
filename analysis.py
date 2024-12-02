from credit import get_all_time_credit_spending
from debit import get_all_time_debit_spending
from schema import CreditTransaction, DebitTransaction


def get_all_time_spending(credit_transactions: list[CreditTransaction], debit_transactions: list[DebitTransaction]) -> float:
    total_spending = 0
    credit_spending = get_all_time_credit_spending(credit_transactions)
    print(f"Total all-time credit spending: ${credit_spending}")
    total_spending += credit_spending
    debit_spending = get_all_time_debit_spending(debit_transactions)
    print(f"Total all-time debit spending: ${debit_spending}")
    total_spending += debit_spending
    return total_spending


