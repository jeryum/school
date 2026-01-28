
import os
from datetime import datetime
import atm_utils

def main():
    print("You need to input your account number, account name and balance to use in the program\n")
    print("WELCOME TO PYTHON ATM MACHINE\n")

    print("Date & Time:", datetime.now())
    print("Operating System:", os.name)

    account_no = input("\nEnter Account Number: ")
    name = input("Enter Account Name: ")
    balance = float(input("Enter Initial Balance: "))

    account = {
        "account_no": account_no,
        "name": name,
        "balance": balance,
        "transactions": []
    }

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account Information")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            atm_utils.check_balance(account)

        elif choice == "2":
            atm_utils.deposit(account)

        elif choice == "3":
            atm_utils.withdraw(account)

        elif choice == "4":
            atm_utils.display_account_info(account)

        elif choice == "5":
            print("\nThank you for using Python ATM Machine!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
