from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.passwordwk as passwordwk_schema
import controllers.passwordwk as passwordwk_controller

import datetime

router = APIRouter()

@router.get("/passwordwk/", response_model=List[passwordwk_schema.PasswordWk])
async def get_all_passwordwk(db: AsyncSession = Depends(get_db)):
    return await passwordwk_controller.get_all_passwordwk(db)

@router.post("/passwordwk/create", response_model=passwordwk_schema.PasswordWk)
async def create_password(pwd: str, app: str, email_address: str, other_info: str, firestoreregflg: str, db: AsyncSession = Depends(get_db)):
    return await passwordwk_controller.create_passwordwk(db, pwd, app, email_address, other_info, firestoreregflg)

# 未登録パスワードのデータを全て削除する
@router.delete("/passwordwk/delete/all", response_model=passwordwk_schema.PasswordWk)
async def delete_passwordwk(db: AsyncSession = Depends(get_db)):
    return await passwordwk_controller.delete_passwordwk(db)

# 登録したパスワードのデータを削除する
@router.delete("/passwordwk/delete", response_model=passwordwk_schema.PasswordWk)
async def delete_passwordwk(app: str, other_info: str, db: AsyncSession = Depends(get_db)):
    return await passwordwk_controller.delete_passwordwk_by_key(db, app, other_info)