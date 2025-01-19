from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class Menu(Base):
    __tablename__ = "menu"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(30), index=True)
    admin = Column(String(1), index=True)
    url = Column(String(15), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)