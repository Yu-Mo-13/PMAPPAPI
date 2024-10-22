from typing import Any, List, Tuple

from sqlalchemy import select, insert, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.autoregist import Autoregist as autoregist_model
import uuid
import datetime

async def get_all_autoregist(db: AsyncSession) -> List[Tuple[uuid.UUID, str, str, str, str]]:
    result: Result = await db.execute(select(
        autoregist_model.uuid,
        autoregist_model.pwd,
        autoregist_model.app,
        autoregist_model.other_info,
        autoregist_model.registered_date
    ))
    return result.all()

# UUIDをキーにして自動登録データを取得
async def get_autoregist_by_uuid(db: AsyncSession, uuid: uuid.UUID) -> List[Tuple[uuid.UUID, str, str, str, str]]:
    result: Result = await db.execute(select(
        autoregist_model.uuid,
        autoregist_model.pwd,
        autoregist_model.app,
        autoregist_model.other_info,
        autoregist_model.registered_date
    ).filter(autoregist_model.uuid == uuid))
    return result.first()

async def create_autoregist(db: AsyncSession, pwd: str, app: str, other_info: str) -> Any:
    result = await db.execute(insert(autoregist_model).values(pwd=pwd, app=app, other_info=other_info, registered_date=datetime.datetime.now()))
    await db.commit()
    return result

# UUIDをキーにして自動登録データを削除
async def delete_autoregist_by_uuid(db: AsyncSession, uuid: uuid.UUID) -> Any:
    result = await db.execute(delete(autoregist_model).where(autoregist_model.uuid == uuid))
    await db.commit()
    return result
