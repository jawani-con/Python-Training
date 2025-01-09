import datetime

class BankAccount:
    def __init__(self):
        self.account = 0
        self.transaction_history = []  

    def deposit(self, amount, transaction_date):
        self.account += amount
        self.transaction_history.append({"type": "Deposit", "amount": amount, "date": transaction_date})
        print(f"'{amount}' added to the Account on {transaction_date}.")
    
    def withdraw(self, amount, transaction_date):
        if amount <= self.account:
            self.account -= amount
            self.transaction_history.append({"type": "Withdrawal", "amount": amount, "date": transaction_date})
            print(f"{amount} withdrawn successfully on {transaction_date}.")
        else:
            print("Withdrawn more than balance available. Enter valid amount")

    def check_balance(self):
        print(f"{self.account} available in account")
    
    def show_transaction_history(self):
        if not self.transaction_history:
            print("No transactions made yet.")
        else:
            print("\nTransaction History:")
            for transaction in self.transaction_history:
                #print(transaction)
                print(f"{transaction['type']} of {transaction['amount']} on {transaction['date']}")

    
class SavingsAccount(BankAccount):
    def __init__(self):
        super().__init__()  # Call the __init__ method of the parent (BankAccount)
        self.interest = 0
    
    def calculate_interest(self):
        if len(self.transaction_history) >= 2:
            for i in range(1, len(self.transaction_history)):
                t1 = self.transaction_history[i-1]
                t2 = self.transaction_history[i]

                date_t1 = t1['date']
                date_t2 = t2['date']

                delta = date_t2 - date_t1
                days=delta.days
                self.interest += ( t1['amount'] * 4 * days) / 36500

            print(self.interest)
        else:
            print("Not enough transactions to calculate the days.")


class CheckingAccount(BankAccount):
    pass

def display_menu():
    print("\nBank Account:")
    print("1. Add deposit")
    print("2. Withdraw")
    print("3. Checking Balance")
    print("4. Show Transaction History")
    print("5. Interest Calculation")
    print("6. Exit")

def get_date_input():
    while True:
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            # Try to convert the string into a date object
            date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
            return date
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

def main():
    acc = SavingsAccount()

    while True:
        display_menu()
        print("Choose an option(1-5): ")

        choice = int(input())

        if choice == 1:
            amount = int(input("Enter the amount for deposit: "))
            date = get_date_input()
            acc.deposit(amount, date)

        elif choice == 2:
            amount = int(input("Enter the amount for withdrawal: "))
            date = get_date_input()  
            acc.withdraw(amount, date)

        elif choice == 3:
            acc.check_balance()

        elif choice == 4:
            acc.show_transaction_history()

        elif choice == 5:
            acc.calculate_interest()

        if choice == 6:
            print("Exiting the Banking system")
            break

main()
