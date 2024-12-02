import csv
from datetime import date, datetime
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
                transaction_date=datetime.strptime(row["Transaction Date"], "%m/%d/%Y").date(),
                transaction_posted_date=datetime.strptime(row["Transaction Posted Date"], "%Y-%m-%d").date(),
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
            total_spending -= transaction.amount
    return round(total_spending, 2)

def get_monthly_credit_breakdown(transactions: list[CreditTransaction]) -> dict[str, dict[str, float]]:
    breakdown: dict[str, dict[str, float]] = {}

    for transaction in transactions:
        month_year_key = f"{transaction.transaction_posted_date.month}-{transaction.transaction_posted_date.year}"
        if month_year_key not in breakdown:
            breakdown[month_year_key] = {}
        if transaction.type not in breakdown[month_year_key]:
            breakdown[month_year_key][transaction.type] = 0
        breakdown[month_year_key][transaction.type] += abs(transaction.amount)

    for month_year in breakdown:
        for transaction_type in breakdown[month_year]:
            breakdown[month_year][transaction_type] = round(breakdown[month_year][transaction_type], 2)
    return breakdown

def get_monthly_credit_transaction_count(transactions: list[CreditTransaction]) -> dict[str, list[CreditTransaction]]:
    breakdown: dict[str, list[CreditTransaction]] = {}
    for transaction in transactions:
        month_year_key = f"{transaction.transaction_posted_date.month}-{transaction.transaction_posted_date.year}"
        if month_year_key not in breakdown:
            breakdown[month_year_key] = []
        breakdown[month_year_key].append(transaction)
    return breakdown
