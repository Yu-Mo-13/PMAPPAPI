from typing import List, Tuple

from sqlalchemy import select, insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.application import Application as application_model

import datetime

async def get_all_application(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        application_model.no,
        application_model.name,
        application_model.accountclas,
        application_model.registered_date
    ))
    return result.all()

async def get_accountclass(db: AsyncSession, app: str) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        application_model.no,
        application_model.name,
        application_model.accountclas,
        application_model.registered_date
    ).filter(application_model.name == app))
    return result.first()

# issue10 データ連動
# no, name, accountclasを登録する
# registered_dateに現在の日付を設定する
async def create_application(db: AsyncSession, no: int , name: str, accountclas: str, registered_date: datetime) -> List[Tuple[int, str, str, datetime.datetime]]:
    result = await db.execute(insert(application_model).values(no=no, name=name, accountclas=accountclas, registered_date=registered_date))
    await db.commit()
    return result