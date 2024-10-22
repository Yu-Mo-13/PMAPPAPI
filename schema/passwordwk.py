from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class PasswordWk(BaseModel):
    no: Optional[int] = Field(None, title="Password number")
    pwd: Optional[str] = Field(None, title="Password")
    app: Optional[str] = Field(None, title="Application name")
    other_info: Optional[str] = Field(None, title="Other information")
    registered_date: Optional[DateTime] = Field(None, title="Registered date")