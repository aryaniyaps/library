from falcon import App
from .books.resources import BookResource


def create_app() -> App:
    """Creates an application instance."""
    app = App()
    register_routes(app)
    return app


def register_routes(app: App) -> None:
    """Registers routes on the application."""
    app.add_route("/books", BookResource())
