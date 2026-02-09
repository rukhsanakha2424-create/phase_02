import os
from collections.abc import Generator
from sqlmodel import Session, SQLModel
from app.db.database import sync_engine

def init_db() -> None:
    """Initialize the database and create tables"""
    SQLModel.metadata.create_all(sync_engine)

def get_session() -> Generator[Session, None, None]:
    """Get a database session"""
    with Session(sync_engine) as session:
        yield session