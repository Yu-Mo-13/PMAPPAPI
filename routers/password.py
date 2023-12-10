from fastapi import APIRouter
import schema.password as password_schema
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from fastapi import Depends
import controllers.password as password_controller

router = APIRouter()

@router.get("/password/app={app}")
async def get_password_no_account(appname: str):
    return {"message": "Hello World"}

@router.get("/password/app={app}/account={account}")
async def get_password(appname: str, account: str):
    return {"message": "Hello World"}

@router.get("/password/", response_model=List[password_schema.Password])
async def get_password(db: AsyncSession = Depends(get_db)):
    return await password_controller.get_all_password(db)