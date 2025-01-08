class ATM:
    def __init__(self):
        self.account = 0

    def deposit(self, amount):
        self.account=self.account+amount
        print(f"'{amount}' added to the Account.")

    def withdraw(self, amount):
        if(amount < self.account):
            self.account=self.account-amount
            print(f"{amount} withdrawn successfully")
        else:
            print("Withdrawn more than balance available. Enter valid amount")


    def check_balance(self):
        print(f"{self.account} available in account")

def display_menu():
    print("\nATM Services:")
    print("1. Add deposit")
    print("2. Withdraw")
    print("3. Checking Balance")
    print("4. Exit")

def main():
    acc=ATM()

    while True:
        display_menu()
        print("Choose an option(1-4): ")

        choice=int(input())

        if choice == 1:
            amount=int(input("Enter the amount for deposit: "))
            acc.deposit(amount)

        if choice == 2:
            amount=int(input("Enter the amount for withdrawal: "))
            acc.withdraw(amount)

        if choice == 3:
            acc.check_balance()

        if choice == 4:
            print("Exiting the ATM system")
            break

main()