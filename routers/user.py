from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.user as user_schema
import controllers.user as user_controller

import datetime
from config import get_config

router = APIRouter()

created_at = datetime.datetime.now()

@router.get("/user/", response_model=List[user_schema.User])
async def get_all_user(db: AsyncSession = Depends(get_db)):
    return await user_controller.get_all_user(db)

@router.get("/user/id={id}", response_model=user_schema.User)
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    return await user_controller.get_user(db, id)

@router.get("/user/engname={engname}&password={password}", response_model=user_schema.User)
async def get_user_by_engname_password(engname: str, password: str, db: AsyncSession = Depends(get_db)):
    return await user_controller.get_user_by_engname_password(db, engname, password)

# ユーザマスタにデータを登録する
@router.post("/user/create/engname={engname}&jpnname={jpnname}&password={password}&authcd={authcd}", response_model=user_schema.User)
async def create_user(engname: str, jpnname: str, password: str, authcd: str, db: AsyncSession = Depends(get_db)):
    return await user_controller.create_user(db, engname, jpnname, password, authcd, str(get_config("ISACTIVE")))

# ユーザマスタのデータを更新する
@router.post("/user/update/id={id}&engname={engname}&jpnname={jpnname}&password={password}&authcd={authcd}", response_model=user_schema.User)
async def update_user(id: int, engname: str, jpnname: str, password: str, authcd: str, db: AsyncSession = Depends(get_db)):
    return await user_controller.update_user(db, id, engname, jpnname, password, authcd)

# ユーザマスタのデータを削除する
@router.post("/user/delete/id={id}", response_model=user_schema.User)
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    return await user_controller.delete_user(db, id, str(get_config("ISDELETE")))