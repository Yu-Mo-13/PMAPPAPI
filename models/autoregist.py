from sqlalchemy import Column, String, DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

from database.database import Base

class Autoregist(Base):
    __tablename__ = "autoregist"
    # uuid
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    pwd = Column(String(200), index=True)
    app = Column(String(200), index=True)
    other_info = Column(String(100), index=True)
    registered_date = Column(DateTime, default=datetime.now)