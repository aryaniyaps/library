from decouple import config


# whether the app is in development.
DEBUG = config("DEBUG", default=False, cast=bool)

# SQLAlchemy database URL.
DATABASE_URL = config("DATABASE_URL")
