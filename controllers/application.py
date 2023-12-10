from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.application import Application as application_model

async def get_all_application(db: AsyncSession) -> List[Tuple[int, str, str, str]]:
    result: Result = await db.execute(select(
        application_model.no,
        application_model.name,
        application_model.accountClas,
        application_model.registered_date
    ))
    return result.all()