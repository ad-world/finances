from schema import CreditTransaction, DebitTransaction, FileType

def detect_file_type(file_name: str) -> FileType:
    with open(file_name, "r") as file:
        first_line = file.readline().strip()
        if "Routing Number" in first_line:
            return FileType.DEBIT
        else:
            return FileType.CREDIT

def print_breakdown(breakdown: dict[str, dict[str, float]]):
    for month_year, types in breakdown.items():
        print(f"{month_year}:")
        for type, amount in types.items():
            print(f"\t{type}: ${amount}")

def print_monthly_debit_transactions(breakdown: dict[str, list[DebitTransaction]]):
    for month_year, transactions in breakdown.items():
        print(f"{month_year}:")
        for transaction in transactions:
            print(f"\t{transaction.transaction_posted_date}: ${transaction.description} ${transaction.amount}")

def print_monthly_credit_transactions(breakdown: dict[str, list[CreditTransaction]]):
    for month_year, transactions in breakdown.items():
        print(f"{month_year}:")
        for transaction in transactions:
            print(f"\t{transaction.transaction_posted_date}: ${transaction.description} ${transaction.amount}")