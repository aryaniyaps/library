import falcon

from .services import BookService


class BookResource:
    """Books resource."""

    def on_get(self, _: falcon.Request, resp: falcon.Response) -> None:
        """Get all available books."""
        resp.body = BookService.get_books()
        resp.status = falcon.HTTP_200

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        """Create a new book."""
        resp.media = BookService.create_book(title=req.media.get("title"))
        resp.status = falcon.HTTP_201
