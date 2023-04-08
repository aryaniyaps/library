from sqlalchemy import create_engine, MetaData

from app.config import DEBUG, DATABASE_URL

metadata = MetaData(
    naming_convention={
        "ix": "index_%(column_0_label)s",
        "uq": "unique_%(table_name)s_%(column_0_name)s",
        "fk": "foreign_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "primary_%(table_name)s",
    },
)

engine = create_engine(url=DATABASE_URL, echo=DEBUG)
