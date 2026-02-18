class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.__isbn = isbn  # Private attribute (Encapsulation)
        self.available = True

    # Getter and Setter for ISBN
    def get_isbn(self):
        return self.__isbn

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def display_info(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.__isbn} | Status: {status}")


class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id  # Private attribute
        self.borrowed_books = []

    # Getter and Setter for Membership ID
    def get_membership_id(self):
        return self.__membership_id

    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} successfully borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently unavailable.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}'.")


# Inheritance: StaffMember inherits from Member
class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library_list, new_book):
        library_list.append(new_book)
        print(f"Staff {self.name} added '{new_book.title}' to the library.")

# --- Quick Test ---
library_collection = []

# 1. Create Staff and Add Books
admin = StaffMember("Alice", "M001", "S123")
b1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-0743273565")
b2 = Book("1984", "George Orwell", "978-0451524935")

admin.add_book(library_collection, b1)
admin.add_book(library_collection, b2)

# 2. Regular Member borrows a book
member1 = Member("Bob", "M002")
member1.borrow_book(b1)

# 3. Check status
b1.display_info()