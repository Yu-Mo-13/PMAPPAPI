from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

import schema.autoregist as autoregist_schema
import controllers.autoregist as autoregist_controller

router = APIRouter()

@router.get("/autoregist/", response_model=List[autoregist_schema.Autoregist])
async def get_all_autoregist(db: AsyncSession = Depends(get_db)):
    return await autoregist_controller.get_all_autoregist(db)

# UUIDをキーにして自動登録データを取得
@router.get("/autoregist/id={uuid}", response_model=autoregist_schema.Autoregist)
async def get_autoregist_by_uuid(uuid: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await autoregist_controller.get_autoregist_by_uuid(db, uuid)

@router.post("/autoregist/create", response_model=autoregist_schema.Autoregist)
async def create_password(pwd: str, app: str, other_info: str, db: AsyncSession = Depends(get_db)):
    return await autoregist_controller.create_autoregist(db, pwd, app, other_info)

# 登録したパスワードのデータを削除する
@router.delete("/autoregist/delete", response_model=autoregist_schema.Autoregist)
async def delete_autoregist(uuid: uuid.UUID, db: AsyncSession = Depends(get_db)):
    return await autoregist_controller.delete_autoregist_by_uuid(db, uuid)