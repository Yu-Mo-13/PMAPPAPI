from typing import Any, List, Tuple

from sqlalchemy import select, insert, func
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.password import Password as password_model
from models.application import Application as application_model
from controllers.generate import Generate
from config import get_config
import datetime

async def get_all_password(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.other_info,
        password_model.registered_date
    ))
    return result.all()

async def get_password_no_account(db: AsyncSession, appname: str) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.other_info,
        password_model.registered_date
    ).order_by(password_model.no.desc()).filter(password_model.app == appname))
    return result.first()

async def get_password(db: AsyncSession, appname: str, account: str) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        password_model.no,
        password_model.pwd,
        password_model.app,
        password_model.other_info,
        password_model.registered_date
    ).order_by(password_model.no.desc()).filter(password_model.app == appname).filter(password_model.other_info == account))
    return result.first()

# issue21 パスワード変更促進
# パスワード変更促進通知が有効なアプリケーションの最新のパスワードを取得する
async def get_notice_passwordlist(db: AsyncSession) -> List[Tuple[str, str, datetime.datetime]]:
    result: Result = await db.execute(select(
        password_model.app,
        password_model.other_info,
        func.max(password_model.registered_date).label('registered_date')
    ).filter(password_model.app.in_(
        select(application_model.name).filter(application_model.noticeclas == get_config('NOTICEFLG'))
    )).group_by(password_model.app, password_model.other_info))
    return result.all()

# 2024/09/16 add nextgen
# ランダム文字列を作成
def create_random_string(markclas: str, length: str) -> str:
    if markclas == '1':
        return Generate(int(length)).generate()
    else:
        return Generate(int(length)).generate_without_symbol()

# issue10 データ連動
# no, pwd, app, email_address, other_info, firestoreregflgを登録する
# registered_dateに現在の日付を設定する
async def create_password(db: AsyncSession, pwd: str, app: str, other_info: str) -> Any:
    result = await db.execute(insert(password_model).values(pwd=pwd, app=app, other_info=other_info, registered_date=datetime.datetime.now()))
    await db.commit()
    return result