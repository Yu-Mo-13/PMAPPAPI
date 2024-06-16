from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class Application(BaseModel):
    no: Optional[int] = Field(None, title="Application number")
    name: Optional[str] = Field(None, title="Application name")
    accountclas: Optional[str] = Field(None, title="Account class")
    noticeclas: Optional[str] = Field(None, title="Notice class")
    registered_date: Optional[DateTime] = Field(None, title="Registered date")