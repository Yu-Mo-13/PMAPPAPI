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

@router.get("/application/app={app}", response_model=application_schema.Application)
async def get_accountclass(app: str, db: AsyncSession = Depends(get_db)):
    return await application_controller.get_accountclass(db, app)
