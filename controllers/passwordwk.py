from typing import Any, List, Tuple

from sqlalchemy import select, insert, delete
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.passwordwk import PasswordWk as passwordwk_model
import datetime

async def get_all_passwordwk(db: AsyncSession) -> List[Tuple[int, str, str, str, str, str, str]]:
    result: Result = await db.execute(select(
        passwordwk_model.no,
        passwordwk_model.pwd,
        passwordwk_model.app,
        passwordwk_model.other_info,
        passwordwk_model.registered_date
    ))
    return result.all()

async def create_passwordwk(db: AsyncSession, pwd: str, app: str, other_info: str) -> Any:
    result = await db.execute(insert(passwordwk_model).values(pwd=pwd, app=app, other_info=other_info, registered_date=datetime.datetime.now()))
    await db.commit()
    return result

# 未登録パスワードのデータを全て削除する
async def delete_passwordwk(db: AsyncSession) -> Any:
    result = await db.execute(delete(passwordwk_model))
    await db.commit()
    return result

# 登録したパスワードのデータを削除する
async def delete_passwordwk_by_key(db: AsyncSession, app: str, other_info: str) -> Any:
    result = await db.execute(delete(passwordwk_model).where(passwordwk_model.app == app).where(passwordwk_model.other_info == other_info))
    await db.commit()
    return result