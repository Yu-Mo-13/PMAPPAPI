from typing import List, Tuple

from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.password import Password as password_model
import datetime

async def get_all_password(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.email_address,
        password_model.other_info,
        password_model.firestoreregflg,
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
        password_model.firestoreregflg,
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
        password_model.firestoreregflg,
        password_model.registered_date
    ).order_by(password_model.no.desc()).filter(password_model.app == appname).filter(password_model.other_info == account))
    return result.first()

# issue10 データ連動
# no, pwd, app, email_address, other_info, firestoreregflgを登録する
# registered_dateに現在の日付を設定する
async def create_password(db: AsyncSession, no: int , pwd: str, app: str, email_address: str, other_info: str, firestoreregflg: str) -> List[Tuple[int, str, str, str, str, str]]:
    result = await db.execute(insert(password_model).values(no=no, pwd=pwd, app=app, email_address=email_address, other_info=other_info, firestoreregflg=firestoreregflg, registered_date=datetime.datetime.now()))
    await db.commit()
    return result