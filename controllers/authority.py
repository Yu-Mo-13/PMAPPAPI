from typing import Any, List, Tuple

from sqlalchemy import select, insert, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.authority import Authority as authority_model
from config import get_config
import datetime

async def get_all_authority(db: AsyncSession) -> List[Tuple[int, str, str, str, datetime.datetime, datetime.datetime]]:
    result: Result = await db.execute(select(
        authority_model.cd,
        authority_model.name,
        authority_model.adminflg,
        authority_model.deleteflg,
        authority_model.created_at,
        authority_model.updated_at
    ).order_by(authority_model.cd).filter(authority_model.deleteflg == get_config("GENERAL", "ISACTIVE")))
    return result.all()

async def get_authority(db: AsyncSession, cd: int) -> Tuple[int, str, str, str, datetime.datetime, datetime.datetime]:
    result: Result = await db.execute(select(
        authority_model.cd,
        authority_model.name,
        authority_model.adminflg,
        authority_model.deleteflg,
        authority_model.created_at,
        authority_model.updated_at
    ).filter(authority_model.cd == cd, authority_model.deleteflg == get_config("GENERAL", "ISACTIVE")))
    return result.first()

# 権限マスタにデータを登録する
async def create_authority(db: AsyncSession, name: str, adminflg: str, deleteflg: str) -> Any:
    result = await db.execute(insert(authority_model).values(name=name, adminflg=adminflg, deleteflg=deleteflg, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()))
    await db.commit()
    return result

# 権限マスタのデータを更新する
async def update_authority(db: AsyncSession, cd: int, name: str, adminflg: str) -> Any:
    result = await db.execute(update(authority_model).values(name=name, adminflg=adminflg, updated_at=datetime.datetime.now()).where(authority_model.cd == cd))
    await db.commit()
    return result

# 権限マスタのデータを削除する
async def delete_authority(db: AsyncSession, cd: int, deleteflg: str) -> Any:
    result = await db.execute(update(authority_model).values(deleteflg=deleteflg, updated_at=datetime.datetime.now()).where(authority_model.cd == cd))
    await db.commit()
    return result