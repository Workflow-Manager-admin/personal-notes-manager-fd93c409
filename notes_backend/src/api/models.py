from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Note(Base):
    """
    SQLAlchemy model for the notes table.
    """
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=False)
    content = Column(Text, nullable=False)
