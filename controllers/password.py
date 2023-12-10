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