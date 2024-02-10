from typing import Any, List, Tuple

from sqlalchemy import select, insert, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User as user_model
from config import get_config
import datetime

async def get_all_user(db: AsyncSession) -> List[Tuple[int, str, str, str, datetime.datetime, datetime.datetime]]:
    result: Result = await db.execute(select(
        user_model.id,
        user_model.engname,
        user_model.jpnname,
        user_model.password,
        user_model.authcd,
        user_model.deleteflg,
        user_model.created_at,
        user_model.updated_at
    ).order_by(user_model.id).filter(user_model.deleteflg == get_config("ISACTIVE")))
    return result.all()

async def get_user(db: AsyncSession, id: int) -> Tuple[int, str, str, str, str, datetime.datetime, datetime.datetime]:
    result: Result = await db.execute(select(
        user_model.id,
        user_model.engname,
        user_model.jpnname,
        user_model.password,
        user_model.authcd,
        user_model.deleteflg,
        user_model.created_at,
        user_model.updated_at
    ).filter(user_model.id == id))
    return result.first()

# ログインで使用する
async def get_user_by_engname_password(db: AsyncSession, engname: str, password: str) -> Tuple[int, str, str, str, str, datetime.datetime, datetime.datetime]:
    result: Result = await db.execute(select(
        user_model.id,
        user_model.engname,
        user_model.jpnname,
        user_model.password,
        user_model.authcd,
        user_model.deleteflg,
        user_model.created_at,
        user_model.updated_at
    ).filter(user_model.engname == engname).filter(user_model.password == password))
    return result.first()

# ユーザマスタにデータを登録する
async def create_user(db: AsyncSession, engname: str, jpnname: str, password: str, authcd: str, deleteflg: str) -> Any:
    result = await db.execute(insert(user_model).values(engname=engname, jpnname=jpnname, password=password, authcd=authcd, deleteflg=deleteflg, created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()))
    await db.commit()
    return result

# ユーザマスタのデータを更新する
async def update_user(db: AsyncSession, id: int, engname: str, jpnname: str, password: str, authcd: str) -> Any:
    result = await db.execute(update(user_model).values(engname=engname, jpnname=jpnname, password=password, authcd=authcd, updated_at=datetime.datetime.now()).where(user_model.id == id))
    await db.commit()
    return result

# ユーザマスタのデータを削除する
async def delete_user(db: AsyncSession, id: int, deleteflg: str) -> Any:
    result = await db.execute(update(user_model).values(deleteflg=deleteflg, updated_at=datetime.datetime.now()).where(user_model.id == id))
    await db.commit()
    return result