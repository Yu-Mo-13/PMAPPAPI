from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.account as account_schema
import controllers.account as account_controller

router = APIRouter()

@router.get("/account/", response_model=List[account_schema.Account])
async def get_all_application(db: AsyncSession = Depends(get_db)):
    return await account_controller.get_all_account(db)

@router.get("/account/app={app}/account={account}", response_model=account_schema.Account)
async def get_application(account: str, app: str, db: AsyncSession = Depends(get_db)):
    return await account_controller.get_account(db, account, app)