import csv
from schema import CreditTransaction, CreditTransactionType


def load_file_credit_transactions(file_path: str) -> list[CreditTransaction]:
    transactions = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(CreditTransaction(
                customer_number=row["Customer Number"],
                account_currency=row["Account Currency"],
                account_number=row["Account Number"],
                account_type=row["Account Type"],
                transaction_date=row["Transaction Date"],
                transaction_posted_date=row["Transaction Posted Date"],
                amount=float(row["Amount"]),
                type=row["Type"],
                description=row["Description"],
                fitid=row["FITID"],
            ))

    return transactions


def load_all_credit_transctions(file_list: list[str]) -> list[CreditTransaction]:
    transactions = []
    for file in file_list:
        transactions.extend(load_file_credit_transactions(file))
    return transactions

def get_all_time_credit_spending(transactions: list[CreditTransaction]) -> float:
    total_spending = 0
    for transaction in transactions:
        if transaction.type == CreditTransactionType.PURCHASE:
            total_spending += abs(transaction.amount)
    return round(total_spending, 2)

