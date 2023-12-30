from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class Account(BaseModel):
    id: Optional[int] = Field(None, title="Account number")
    account: Optional[str] = Field(None, title="Account")
    app: Optional[str] = Field(None, title="Application name")
    deleteflg: Optional[str] = Field(None, title="Delete flag")
    created_at: Optional[DateTime] = Field(None, title="Created date")
    updated_at: Optional[DateTime] = Field(None, title="Updated date")