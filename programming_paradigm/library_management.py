class Book:
    def __init__(self, title, author):
        self.title = title          # Public attribute
        self.author = author        # Public attribute
        self._is_checked_out = False   # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []  # Private list of Book objects

    def add_book(self, book):
        """Add a new Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """Print all available books."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
