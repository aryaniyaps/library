from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.core.database import metadata

books_table = Table(
    "books", metadata, 
    Column(
        "id", 
        Integer, 
        primary_key=True
    ), 
    Column(
        "title", 
        String(255), 
        nullable=False
    ), 
    Column(
        "isbn_code", 
        Integer(13), 
        nullable=False
    ), 
    Column(
        "created_at", 
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    ),
    Column(
        "updated_at", 
        DateTime(timezone=True), 
        server_default=func.now(), 
        nullable=False
    ),
)