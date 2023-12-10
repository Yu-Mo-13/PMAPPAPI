from typing import Optional, List
from fastapi import APIRouter
import schema.application as application_schema
import controllers.application as application_controller
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import get_db
from fastapi import Depends

router = APIRouter()

@router.get("/application/app={app}", response_model=application_schema.Application)
async def get_accountclass(app: str):
    return [application_schema.Application(no=1, name=app, accountClas="test", registered_date="test")]

@router.get("/application/", response_model=List[application_schema.Application])
async def get_accountclass(db: AsyncSession = Depends(get_db)):
    return await application_controller.get_all_application(db)
