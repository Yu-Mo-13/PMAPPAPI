from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    account = Column(String(100), index=True)
    app = Column(String(100), index=True)
    deleteflg = Column(String(1), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)