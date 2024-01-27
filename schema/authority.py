from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class Authority(BaseModel):
    cd: Optional[int] = Field(None, title="Authority code")
    name: Optional[str] = Field(None, title="Authority name")
    adminflg: Optional[str] = Field(None, title="Admin flag")
    deleteflg: Optional[str] = Field(None, title="Delete flag")
    created_at: Optional[DateTime] = Field(None, title="Created date")
    updated_at: Optional[DateTime] = Field(None, title="Updated date")