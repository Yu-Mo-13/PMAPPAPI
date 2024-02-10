from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from config import get_config
import datetime

import schema.account as account_schema
import controllers.account as account_controller

router = APIRouter()

created_at = datetime.datetime.now()

@router.get("/account/", response_model=List[account_schema.Account])
async def get_all_account(db: AsyncSession = Depends(get_db)):
    return await account_controller.get_all_account(db)

@router.get("/account/app={app}", response_model=List[account_schema.Account])
async def get_all_account_by_appname(app: str, db: AsyncSession = Depends(get_db)):
    return await account_controller.get_all_account_by_appname(db, app)

@router.get("/account/app={app}/account={account}", response_model=account_schema.Account)
async def get_account(account: str, app: str, db: AsyncSession = Depends(get_db)):
    return await account_controller.get_account(db, account, app)

@router.post("/account/create/app={app}/account={account}", response_model=account_schema.Account)
async def insert_account(account: str, app: str, db: AsyncSession = Depends(get_db)):
    return await account_controller.create_account(db, account, app, str(get_config("ISACTIVE")), created_at)

@router.post("/account/delete/app={app}/account={account}", response_model=account_schema.Account)
async def delete_account(account: str, app: str, db: AsyncSession = Depends(get_db)):
    return await account_controller.delete_account(db, account, app, str(get_config("ISDELETE")), created_at)