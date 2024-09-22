from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from config import get_config
import datetime

import schema.otpctl as otpctl_schema
import controllers.otpctl as otpctl_controller

router = APIRouter()

created_at = datetime.datetime.now()

@router.get("/otpctl", response_model=List[otpctl_schema.OtpCtl])
async def get_all_otpctl(db: AsyncSession = Depends(get_db)):
    return await otpctl_controller.get_all_otpctl(db)

@router.get("/otpctl/cd={cd}", response_model=otpctl_schema.OtpCtl)
async def get_otpctl_value_by_cd(cd: str, db: AsyncSession = Depends(get_db)):
    return await otpctl_controller.get_otpctl_value_by_cd(db, cd)

@router.put("/otpctl/cd={cd}", response_model=otpctl_schema.OtpCtl)
async def update_otpctl_by_cd(cd: str, value: str, db: AsyncSession = Depends(get_db)):
    updated_at = datetime.datetime.now()
    return await otpctl_controller.update_otpctl_by_cd(db, cd, value, updated_at)