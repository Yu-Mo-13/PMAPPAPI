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

# issue21 パスワード変更促進
@router.get("/password/notice", response_model=List[password_schema.Password])
async def get_notice_passwordlist(db: AsyncSession = Depends(get_db)):
    return await password_controller.get_notice_passwordlist(db)

# 2024/09/16 add nextgen
# ランダム文字列を作成
@router.get("/password/generate/markclas={markclas}&length={length}", response_model=str)
def create_random_string(markclas: str, length: str):
    return password_controller.create_random_string(markclas, length)

# issue10 データ連動
@router.post("/password/create", response_model=password_schema.Password)
async def create_password(pwd: str, app: str, other_info: str, db: AsyncSession = Depends(get_db)):
    return await password_controller.create_password(db, pwd, app, other_info)
