from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class OtpCtl(BaseModel):
    cd: Optional[str] = Field(None, title="Control code")
    name: Optional[str] = Field(None, title="Control name")
    value: Optional[str] = Field(None, title="Control value")
    remarks: Optional[str] = Field(None, title="Remarks")
    created_at: Optional[DateTime] = Field(None, title="Created date")
    updated_at: Optional[DateTime] = Field(None, title="Updated date")