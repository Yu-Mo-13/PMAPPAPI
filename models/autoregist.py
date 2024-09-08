from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from database.database import Base

class Autoregist(Base):
    __tablename__ = "autoregist"
    # uuid
    uuid = Column(String(36), primary_key=True, index=True)
    pwd = Column(String(200), index=True)
    app = Column(String(200), index=True)
    other_info = Column(String(100), index=True)
    registered_date = Column(DateTime, default=datetime.now)