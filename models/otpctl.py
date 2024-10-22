from sqlalchemy import Column, String, DateTime
from datetime import datetime

from database.database import Base

class OtpCtl(Base):
    __tablename__ = "otpctl"
    cd = Column(String(2), primary_key=True, index=True)
    name = Column(String(30), index=True)
    value = Column(String(30), index=True)
    remarks = Column(String(50), index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)