from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.password as password_schema
import controllers.password as password_controller

router = APIRouter()

@router.get("/password/", response_model=List[password_schema.Password])
async def get_password(db: AsyncSession = Depends(get_db)):
    return await password_controller.get_all_password(db)

@router.get("/password/app={appname}", response_model=password_schema.Password)
async def get_password_no_account(appname: str, db: AsyncSession = Depends(get_db)):
    return await password_controller.get_password_no_account(db, appname)

@router.get("/password/app={appname}/account={account}", response_model=password_schema.Password)
async def get_password(appname: str, account: str, db: AsyncSession = Depends(get_db)):
    return await password_controller.get_password(db, appname, account)