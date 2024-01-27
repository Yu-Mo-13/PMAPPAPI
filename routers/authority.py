from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.authority as authority_schema
import controllers.authority as authority_controller

import datetime
from config import get_config

router = APIRouter()

created_at = datetime.datetime.now()

@router.get("/authority/", response_model=List[authority_schema.Authority])
async def get_all_authority(db: AsyncSession = Depends(get_db)):
    return await authority_controller.get_all_authority(db)

@router.get("/authority/cd={cd}", response_model=authority_schema.Authority)
async def get_authority(cd: int, db: AsyncSession = Depends(get_db)):
    return await authority_controller.get_authority(db, cd)

# 権限データを登録する
@router.post("/authority/create/name={name}&adminflg={adminflg}", response_model=authority_schema.Authority)
async def create_authority(name: str, adminflg: str, db: AsyncSession = Depends(get_db)):
    return await authority_controller.create_authority(db, name, adminflg, str(get_config("GENERAL", "ISACTIVE")))

# 権限データを更新する
@router.post("/authority/update/cd={cd}&name={name}&adminflg={adminflg}", response_model=authority_schema.Authority)
async def update_authority(cd: int, name: str, adminflg: str, db: AsyncSession = Depends(get_db)):
    return await authority_controller.update_authority(db, cd, name, adminflg)

# 権限データを削除する
@router.post("/authority/delete/cd={cd}", response_model=authority_schema.Authority)
async def delete_authority(cd: int, db: AsyncSession = Depends(get_db)):
    return await authority_controller.delete_authority(db, cd, str(get_config("GENERAL", "ISDELETE")))