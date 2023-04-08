from app.books.repos import BookRepo


class BookService:
    """Books service."""

    @classmethod
    def get_books(cls):
        """Get all available books."""
        return BookRepo.get_books()

    @classmethod
    def create_book(cls, title: str):
        """Create a new book."""
        return BookRepo.create_book(title=title)
