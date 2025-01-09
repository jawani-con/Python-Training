class LibraryCatalog:
    def __init__(self):
        self.books = []  

    def add_book(self, title, author, category):
        self.books.append({
            "title": title,
            "author": author,
            "category": category
        })
        print(f"Book '{title}' added successfully.")

    def search_by_title(self, title):
        results = [book for book in self.books if book["title"].lower() == title.lower()]
        self.display_results(results)

    def search_by_author(self, author):
        results = [book for book in self.books if book["author"].lower() == author.lower()]
        self.display_results(results)

    def search_by_category(self, category):
        results = [book for book in self.books if book["category"].lower() == category.lower()]
        self.display_results(results)

    def display_results(self, results):
        if results:
            print("\nSearch Results:")
            for idx, book in enumerate(results, 1):
                print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Category: {book['category']}")
        else:
            print("\nNo books found matching your search criteria.")

    def display_all_books(self):
        if self.books:
            print("\nLibrary Catalog:")
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Category: {book['category']}")
        else:
            print("\nThe catalog is empty.")

def display_menu():
    print("\nLibrary Catalog System")
    print("1. Add Book")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Category")
    print("5. Display All Books")
    print("6. Exit")

def main():
    catalog = LibraryCatalog()

    while True:
        display_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            category = input("Enter book category: ")
            catalog.add_book(title, author, category)

        elif choice == "2":
            title = input("Enter the title to search for: ")
            catalog.search_by_title(title)

        elif choice == "3":
            author = input("Enter the author to search for: ")
            catalog.search_by_author(author)

        elif choice == "4":
            category = input("Enter the category to search for: ")
            catalog.search_by_category(category)

        elif choice == "5":
            catalog.display_all_books()

        elif choice == "6":
            print("Thanks for using the Library Catalog System!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
