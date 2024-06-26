from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.application as application_schema
import controllers.application as application_controller

router = APIRouter()

@router.get("/application/", response_model=List[application_schema.Application])
async def get_all_application(db: AsyncSession = Depends(get_db)):
    return await application_controller.get_all_application(db)

# issue18 デスクトップアプリ版API移行
@router.get("/application/search/app={app}", response_model=application_schema.Application)
async def get_application(app: str, db: AsyncSession = Depends(get_db)):
    return await application_controller.get_application(db, app)

@router.get("/application/app={app}", response_model=application_schema.Application)
async def get_accountclass(app: str, db: AsyncSession = Depends(get_db)):
    return await application_controller.get_accountclass(db, app)

# issue10 データ連動
@router.post("/application/create", response_model=application_schema.Application)
async def create_application(name: str, accountclass: str, noticeclass: str, db: AsyncSession = Depends(get_db)):
    return await application_controller.create_application(db, name, accountclass, noticeclass)

# issue18 デスクトップアプリ版API移行
@router.post("/application/update", response_model=application_schema.Application)
async def update_application(no: int, accountclass: str, noticeclass: str, db: AsyncSession = Depends(get_db)):
    return await application_controller.update_application(db, no, accountclass, noticeclass)