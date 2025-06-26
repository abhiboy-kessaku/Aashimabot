class Book:
    def __init__(self, name, author, price, pages):
        self.name = name
        self.author = author
        self.price = price
        self.pages = pages

    def display(self):
        print(f"Name: {self.name}, Author: {self.author}, Price: ₹{self.price}, Pages: {self.pages}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, author, price, pages):
        book = Book(name, author, price, pages)
        self.books.append(book)
        print(f"Book '{name}' added to the library.")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nAll Books in the Library:")
            for book in self.books:
                book.display()

    def search_book(self, name):
        found = False
        for book in self.books:
            if book.name.lower() == name.lower():
                print("Book Found:")
                book.display()
                found = True
                break
        if not found:
            print("Book not found.")

    def remove_book(self, name):
        for book in self.books:
            if book.name.lower() == name.lower():
                self.books.remove(book)
                print(f"Book '{name}' removed from the library.")
                return
        print("Book not found to remove.")


# Main Program
def main():
    lib = Library()

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book by Name")
        print("4. Remove Book by Name")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter book name: ")
            author = input("Enter author name: ")
            price = float(input("Enter price: ₹"))
            pages = int(input("Enter number of pages: "))
            lib.add_book(name, author, price, pages)

        elif choice == '2':
            lib.view_books()

        elif choice == '3':
            name = input("Enter book name to search: ")
            lib.search_book(name)

        elif choice == '4':
            name = input("Enter book name to remove: ")
            lib.remove_book(name)

        elif choice == '5':
            print("Exiting Library. Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
