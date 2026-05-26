from sqlalchemy import Column, String, Integer, ForeignKey
from app.database.db import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"))