from typing import List, Tuple, Dict

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.menu import Menu as menu_model
from datetime import datetime
from config import get_config

async def get_all_menu(db: AsyncSession) -> List[Dict[str, str]]:
    result: Result = await db.execute(select(
        menu_model.id,
        menu_model.name,
        menu_model.admin,
        menu_model.url,
        menu_model.created_at,
        menu_model.updated_at
    ).filter(menu_model.admin != get_config('ISADMIN')).order_by(menu_model.id))
    menu_data = result.fetchall()
    return await transform_menu_data(menu_data)

async def get_admin_menu(db: AsyncSession) -> List[Dict[str, str]]:
    result: Result = await db.execute(select(
        menu_model.id,
        menu_model.name,
        menu_model.admin,
        menu_model.url,
        menu_model.created_at,
        menu_model.updated_at
    ).order_by(menu_model.id))
    menu_data = result.fetchall()
    return await transform_menu_data(menu_data)

# get_all_menuとget_admin_menuの返却結果からidとnameとurlのみを取得する
async def transform_menu_data(menu_data: List[Tuple[int, str, str, str, datetime, datetime]]) -> List[Dict[str, str]]:
    return [{"id": id, "name": name, "url": url} for id, name, _, url, _, _ in menu_data]