from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field, UUID4

class Autoregist(BaseModel):
    uuid: Optional[UUID4] = Field(None, title="UUID")
    pwd: Optional[str] = Field(None, title="Password")
    app: Optional[str] = Field(None, title="Application name")
    other_info: Optional[str] = Field(None, title="Other information")
    registered_date: Optional[DateTime] = Field(None, title="Registered date")