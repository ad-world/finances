import os

from analysis import get_all_time_spending
from credit import load_all_credit_transctions
from debit import get_all_time_earnings, load_all_debit_transctions

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
        if file.endswith(".csv"):
            if file.endswith("credit.csv"):
                credit_files.append(os.path.join(data_directory, file))
            elif file.endswith("debit.csv"):
                debit_files.append(os.path.join(data_directory, file))
    print("Found credit files:")
    for file in credit_files:
        print(f"\t{file}")
    print("Found debit files:")
    for file in debit_files:
        print(f"\t{file}")
    
    print("\nLoading transactions...\n")

    credit_transactions = load_all_credit_transctions(credit_files)
    debit_transactions = load_all_debit_transctions(debit_files)

    print(f"Total all-time spending: ${get_all_time_spending(credit_transactions, debit_transactions)}")
    print(f"Total all-time earnings: ${get_all_time_earnings(debit_transactions)}")

    return 0

if __name__ == "__main__":
    main()