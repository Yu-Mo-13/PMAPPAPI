from typing import List
from fastapi import APIRouter, Depends
from database.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

import schema.menu as menu_schema
import controllers.menu as menu_controller

router = APIRouter()

@router.get("/menu", response_model=List[menu_schema.Menu])
async def get_all_menu(db: AsyncSession = Depends(get_db)):
    return await menu_controller.get_all_menu(db)

@router.get("/menu/admin", response_model=List[menu_schema.Menu])
async def get_admin_menu(db: AsyncSession = Depends(get_db)):
    return await menu_controller.get_admin_menu(db)