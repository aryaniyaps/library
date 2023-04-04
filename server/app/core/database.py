from sqlalchemy import create_engine, MetaData

from app.config import DEBUG, DATABASE_URL

metadata = MetaData()

engine = create_engine(url=DATABASE_URL, echo=DEBUG)