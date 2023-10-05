class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print("This book is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print("This book is already available.")


# Sample usage
if __name__ == "__main__":
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    book1.borrow()
    book1.borrow()  # Trying to borrow again

    book2.borrow()
    book2.return_book()
    book2.return_book()  # Trying to return again
