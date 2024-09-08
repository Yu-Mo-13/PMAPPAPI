from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class Application(BaseModel):
    no: Optional[int] = Field(None, title="Application number")
    name: Optional[str] = Field(None, title="Application name")
    accountclas: Optional[str] = Field(None, title="Account class")
    noticeclas: Optional[str] = Field(None, title="Notice class")
    markclas: Optional[str] = Field(None, title="Mark class")
    autosize: Optional[str] = Field(None, title="Auto size")
    registered_date: Optional[DateTime] = Field(None, title="Registered date")