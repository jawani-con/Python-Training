class Inventory:
    def __init__(self):
        self.stocks = {}

    def add_inventory(self, item, quantity):
        if item in self.stocks:
            self.stocks[item] += quantity
        else:
            self.stocks[item] = quantity

    def remove_inventory(self, item, quantity):
        if item not in self.stocks:
            print("Item not present in inventory")
        elif self.stocks[item] < quantity:
            print("The required quantity of item not present")
        else:
            self.stocks[item] -= quantity
            print(f"{quantity} of {item} removed from inventory")

    def query_items(self, item):
        if item not in self.stocks:
            print("Item not present in inventory")
        else:
            print(f"{item} present in {self.stocks[item]}")


def display_menu():
    print("Inventory Management")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Check for item in inventory")
    print("4. Exit")

def main():
    invent = Inventory()  # Create an instance of Inventory

    while True:
        display_menu()  # Display the menu
        choice = int(input("Choose an option (1-4): "))  # Take user input for menu option

        if choice == 1:
            item = input("Enter the item you want to add: ")
            quantity = int(input("Enter the quantity of the item: "))
            invent.add_inventory(item, quantity)

        elif choice == 2:
            item = input("Enter the item you want to remove: ")
            quantity = int(input("Enter the quantity of the item: "))
            invent.remove_inventory(item, quantity)

        elif choice == 3:
            item = input("Enter the item you want to query: ")
            invent.query_items(item)

        elif choice == 4:
            print("Thank you for using the inventory system!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
