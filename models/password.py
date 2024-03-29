from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.orm import relationship
from datetime import datetime

from database.database import Base

class Password(Base):
    __tablename__ = "password"
    no = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pwd = Column(String(200), index=True)
    app = Column(String(200), index=True)
    email_address = Column(String(100), index=True, default='')
    other_info = Column(String(100), index=True)
    firestoreregflg = Column(String(1), index=True, default='0')
    registered_date = Column(DateTime, default=datetime.now)