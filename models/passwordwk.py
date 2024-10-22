from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class PasswordWk(Base):
    __tablename__ = "passwordwk"
    no = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pwd = Column(String(200), index=True)
    app = Column(String(200), index=True)
    other_info = Column(String(100), index=True)
    registered_date = Column(DateTime, default=datetime.now)