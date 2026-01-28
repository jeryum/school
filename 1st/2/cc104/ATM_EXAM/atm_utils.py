
import math
from datetime import datetime

transaction_types = set()

def check_balance(account):
    account["last_checked"] = datetime.now()
    print(f"\nCurrent Balance: {account['balance']:.2f}")
    transaction_types.add("Check Balance")

def deposit(account):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid deposit amount.")
            return

        account["balance"] += amount
        account["balance"] = math.floor(account["balance"] * 100) / 100
        account["transactions"].append(("Deposit", amount, datetime.now()))
        transaction_types.add("Deposit")

        print("Deposit successful!")
        print(f"Current Balance: {account['balance']:.2f}")

    except ValueError:
        print("Invalid input. Please enter a number.")

def withdraw(account):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid withdrawal amount.")
            return

        if amount > account["balance"]:
            print("Insufficient balance.")
            return

        account["balance"] -= amount
        account["balance"] = math.floor(account["balance"] * 100) / 100
        account["transactions"].append(("Withdraw", amount, datetime.now()))
        transaction_types.add("Withdraw")

        print("Withdrawal successful!")
        print(f"Current Balance: {account['balance']:.2f}")

    except ValueError:
        print("Invalid input. Please enter a number.")

def display_account_info(account):
    print("\nAccount Number:", account["account_no"])
    print("Account Name:", account["name"])
    print(f"Balance: {account['balance']:.2f}")
    print("Transactions:", transaction_types)
    print("Last Checked:", account.get("last_checked", "Not yet checked"))
