from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.password import Password as password_model

async def get_all_password(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.email_address,
        password_model.other_info,
        password_model.firestoreRegFlg,
        password_model.registered_date
    ))
    return result.all()

async def get_password_no_account(db: AsyncSession, appname: str) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.email_address,
        password_model.other_info,
        password_model.firestoreRegFlg,
        password_model.registered_date
    ).order_by(password_model.no.desc()).filter(password_model.app == appname))
    return result.first()

async def get_password(db: AsyncSession, appname: str, account: str) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.email_address,
        password_model.other_info,
        password_model.firestoreRegFlg,
        password_model.registered_date
    ).order_by(password_model.no.desc()).filter(password_model.app == appname).filter(password_model.other_info == account))
    return result.first()
