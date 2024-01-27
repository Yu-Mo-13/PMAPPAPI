from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class User(BaseModel):
    id: Optional[int] = Field(None, title="User id")
    password: Optional[str] = Field(None, title="User password")
    engname: Optional[str] = Field(None, title="User name in English")
    jpnname: Optional[str] = Field(None, title="User name in Japanese")
    authcd: Optional[str] = Field(None, title="Authority code")
    deleteflg: Optional[str] = Field(None, title="Delete flag")
    created_at: Optional[DateTime] = Field(None, title="Created date")
    updated_at: Optional[DateTime] = Field(None, title="Updated date")