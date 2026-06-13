# Class definition for Book
class Book:
    # Constructor to initialize attributes
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.borrowed_copies = 0

    # Method to calculate available copies
    def available_copies(self):
        return self.total_copies - self.borrowed_copies

    # Method to borrow a book
    def borrow_book(self):
        if self.available_copies() > 0:
            self.borrowed_copies += 1
            print(f"\nBook borrowed successfully: {self.title}")
            print(f"Available copies now: {self.available_copies()}")
        else:
            print("\nSorry, this book is not available.")

    # Method to return a book
    def return_book(self):
        if self.borrowed_copies > 0:
            self.borrowed_copies -= 1
            print(f"\nBook returned successfully: {self.title}")
            print(f"Available copies now: {self.available_copies()}")
        else:
            print("\nNo borrowed copies to return.")

    # Method to display book information
    def display_info(self):
        print(f"{self.title} by {self.author} | Available copies: {self.available_copies()}")


# Main Program

# List to store Book objects
library = []

# Input number of books
num_books = int(input("How many books do you want to enter? "))

# Loop to enter book details
for i in range(1, num_books + 1):
    print()
    title = input(f"Enter title for book {i}: ")
    author = input(f"Enter author for book {i}: ")
    copies = int(input("Enter number of copies: "))

    # Create Book object and store in list
    book = Book(title, author, copies)
    library.append(book)

# Menu loop
while True:
    print("\nMenu:")
    print("1. Display all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")

    choice = int(input("Menu choice: "))

    if choice == 1:
        print("\nLibrary Book List:")
        for i in range(len(library)):
            print(f"{i + 1}. ", end="")
            library[i].display_info()

    elif choice == 2:
        book_num = int(input("Enter book number to borrow: "))
        if 1 <= book_num <= len(library):
            library[book_num - 1].borrow_book()
        else:
            print("Invalid book number.")

    elif choice == 3:
        book_num = int(input("Enter book number to return: "))
        if 1 <= book_num <= len(library):
            library[book_num - 1].return_book()
        else:
            print("Invalid book number.")

    elif choice == 4:
        print("\nThank you for using the library system.")
        break

    else:
        print("Invalid choice. Please try again.")