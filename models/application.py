from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class Application(Base):
    __tablename__ = "application"
    no = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), index=True)
    accountclas = Column(String(1), index=True)
    noticeclas = Column(String(1), index=True)
    markclas = Column(String(1), index=True)
    autosize = Column(String(2), index=True)
    registered_date = Column(DateTime, default=datetime.now)