class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False   # private attribute

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

    def __str__(self):
        status = "Available" if self.is_available() else "Checked Out"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self._books = []   # private list of books

    def add_book(self, book):
        """Add a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return f"'{title}' has been checked out."
        return f"'{title}' is not available."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return f"'{title}' has been returned."
        return f"'{title}' was not checked out from this library."

    def list_available_books(self):
        """List all books that are not checked out."""
        available = [book for book in self._books if book.is_available()]
        if not available:
            return "No books available."
        return "\n".join(str(book) for book in available)