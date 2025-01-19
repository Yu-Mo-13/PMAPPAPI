from typing import Optional
from datetime import datetime as DateTime
from pydantic import BaseModel, Field

class Menu(BaseModel):
    id: Optional[int] = Field(None, title="ID")
    name: Optional[str] = Field(None, title="Menu name")
    url: Optional[str] = Field(None, title="URL")
