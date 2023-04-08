from app.core.database import engine
from .tables import books_table


class BookRepo:
    """Books repository."""

    @classmethod
    def get_books(cls):
        """Get all available books."""
        with engine.connect() as connection:
            return connection.execute(books_table.select())

    @classmethod
    def create_book(cls, title: str):
        """Create a new book."""
        with engine.begin() as connection:
            result = connection.execute(books_table.insert(), {"title": title})
        return result
