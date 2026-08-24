class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}")


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")

    def register_patron(self):
        patron_id = input("Enter Patron ID: ")
        name = input("Enter Patron Name: ")
        patron = Patron(patron_id, name)
        self.patrons.append(patron)
        print("Patron registered successfully!")

    def issue_book(self):
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book and patron:
            if book.available:
                book.available = False
                patron.borrow_book(book)
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Invalid Book ID or Patron ID.")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        patron_id = input("Enter Patron ID: ")

        book = None
        patron = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for p in self.patrons:
            if p.patron_id == patron_id:
                patron = p
                break

        if book and patron:
            if not book.available:
                book.available = True
                patron.return_book(book)
                print("Book returned successfully!")
            else:
                print("Book is already available.")
        else:
            print("Invalid Book ID or Patron ID.")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                book.display()


library = Library()

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.register_patron()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")