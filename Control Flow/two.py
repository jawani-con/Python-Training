class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' added to the library.")

    def remove_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"'{book_name}' removed from the library.")
        else:
            print(f"'{book_name}' not found in the library.")

    def search_book(self, book_name):
        if book_name in self.books:
            print(f"'{book_name}' is available in the library.")
        else:
            print(f"'{book_name}' is not found in the library.")

    def list_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(f"- {book}")

def display_menu():
    print("\nLibrary Menu:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search a Book")
    print("4. List All Books")
    print("5. Exit")

def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            book_name = input("Enter the book name to add: ")
            library.add_book(book_name)
        elif choice == "2":
            book_name = input("Enter the book name to remove: ")
            library.remove_book(book_name)
        elif choice == "3":
            book_name = input("Enter the book name to search: ")
            library.search_book(book_name)
        elif choice == "4":
            library.list_books()
        elif choice == "5":
            print("Exiting the program. Thank you for using the library system!")
            break
        else:
            print("Invalid option, please choose a number between 1 and 5.")

main()
