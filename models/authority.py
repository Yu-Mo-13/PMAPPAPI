from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class Authority(Base):
    __tablename__ = "authority"
    cd = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(30), index=True)
    adminflg = Column(String(1), index=True)
    deleteflg = Column(String(1), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)