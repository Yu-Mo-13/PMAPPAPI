from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class Password(BaseModel):
    no: Optional[int] = Field(None, title="Password number")
    pwd: Optional[str] = Field(None, title="Password")
    app: Optional[str] = Field(None, title="Application name")
    email_address: Optional[str] = Field(None, title="Email address")
    other_info: Optional[str] = Field(None, title="Other information")
    firestoreregflg: Optional[str] = Field(None, title="Firestore registration flag")
    registered_date: Optional[DateTime] = Field(None, title="Registered date")