from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class User(Base):
    __tablename__ = "muser"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    engname = Column(String(15), index=True)
    jpnname = Column(String(20), index=True)
    password = Column(String(20), index=True)
    authcd = Column(String(1), index=True)
    deleteflg = Column(String(1), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)