import os

from analysis import get_all_time_spending
from credit import get_monthly_credit_breakdown, get_monthly_credit_transaction_count, load_all_credit_transctions
from debit import get_all_time_earnings, get_monthly_debit_breakdown, get_monthly_debit_transaction_count, load_all_debit_transctions
from schema import FileType
from util import detect_file_type, print_breakdown, print_monthly_credit_transactions, print_monthly_debit_transactions

def print_prologue():
    print("Personal Finances")
    print("\tby: @ad-world")
    print("=================")

def main():
    print_prologue()
    data_directory = input("Enter data directory: ")
    if not os.path.exists(data_directory):
        print("Data directory does not exist")

    credit_files = []
    debit_files = []

    for file in os.listdir(data_directory):
        if not file.endswith(".csv"):
            continue
        file_type = detect_file_type(os.path.join(data_directory, file))
        if file_type == FileType.CREDIT:
            credit_files.append(os.path.join(data_directory, file))
        elif file_type == FileType.DEBIT:
            debit_files.append(os.path.join(data_directory, file))
        else:
            print(f"Unknown file type for {file}")
            continue

    for file in credit_files:
        print(f"Loading {file}...")
    for file in debit_files:
        print(f"Loading {file}...")
    
    print("\nLoading transactions...\n")

    credit_transactions = load_all_credit_transctions(credit_files)
    debit_transactions = load_all_debit_transctions(debit_files)

    print(f"Total all-time spending: ${get_all_time_spending(credit_transactions, debit_transactions)}")
    print(f"Total all-time earnings: ${get_all_time_earnings(debit_transactions)}")

    monthly_debit_breakdown = get_monthly_debit_breakdown(debit_transactions)
    monthly_credit_breakdown = get_monthly_credit_breakdown(credit_transactions)

    print("\nMonthly Debit Breakdown:")
    print_breakdown(monthly_debit_breakdown)
    print("\nMonthly Credit Breakdown:")
    print_breakdown(monthly_credit_breakdown)

    monthly_debit_transactions = get_monthly_debit_transaction_count(debit_transactions)
    monthly_credit_transactions = get_monthly_credit_transaction_count(credit_transactions)

    print("\nMonthly Debit Transactions:")
    print_monthly_debit_transactions(monthly_debit_transactions)
    print("\nMonthly Credit Transactions:")
    print_monthly_credit_transactions(monthly_credit_transactions)

    return 0

if __name__ == "__main__":
    main()