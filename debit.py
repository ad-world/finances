import csv
from datetime import date, datetime
from schema import DebitTransaction, DebitTransactionType


def load_file_debit_transactions(file_path: str) -> list[DebitTransaction]:
    transactions = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            transactions.append(DebitTransaction(
                customer_number=row["Customer Number"],
                account_currency=row["Account Currency"],
                routing_number=row["Routing Number"],
                account_number=row["Account Number"],
                account_type=row["Account Type"],
                transaction_posted_date=datetime.strptime(row["Transaction Posted Date"], "%m/%d/%Y").date(),
                transaction_posted_time=row["Transaction Posted Time"],
                amount=float(row["Amount"]),
                type=row["Type"],
                description=row["Description"],
                fitid=row["FITID"],
            ))
    return transactions


def load_all_debit_transctions(file_list: list[str]) -> list[DebitTransaction]:
    transactions = []
    for file in file_list:
        transactions.extend(load_file_debit_transactions(file))
    return transactions


def get_all_time_debit_spending(transactions: list[DebitTransaction]) -> float:
    total_spending = 0
    for transaction in transactions:
        if transaction.type == DebitTransactionType.WITHDRAWAL:
            total_spending += abs(transaction.amount)

    return total_spending


def get_all_time_earnings(transactions: list[DebitTransaction]) -> float:
    total_earnings = 0
    for transaction in transactions:
        if transaction.type == DebitTransactionType.DEPOSIT:
            total_earnings += transaction.amount
    return round(total_earnings, 2)

def get_monthly_debit_breakdown(transactions: list[DebitTransaction]) -> dict[str, dict[str, float]]:
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


def get_monthly_debit_transaction_count(transactions: list[DebitTransaction]) -> dict[str, list[DebitTransaction]]:
    breakdown: dict[str, list[DebitTransaction]] = {}
    for transaction in transactions:
        month_year_key = f"{transaction.transaction_posted_date.month}-{transaction.transaction_posted_date.year}"
        if month_year_key not in breakdown:
            breakdown[month_year_key] = []
        breakdown[month_year_key].append(transaction)
    return breakdown
