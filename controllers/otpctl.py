from typing import Any, List, Tuple

from sqlalchemy import select, update
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.otpctl import OtpCtl as otpctl_model
from datetime import datetime

async def get_all_otpctl(db: AsyncSession) -> List[Tuple[str, str, str, str, datetime, datetime]]:
    result: Result = await db.execute(select(
        otpctl_model.cd,
        otpctl_model.name,
        otpctl_model.value,
        otpctl_model.remarks,
        otpctl_model.created_at,
        otpctl_model.updated_at
    ))
    return result.all()

async def get_otpctl_value_by_cd(db: AsyncSession, cd: str) -> List[Tuple[str, str]]:
    result: Result = await db.execute(select(
        otpctl_model.cd,
        otpctl_model.value
    ).filter(otpctl_model.cd == cd))
    return result.first()

async def update_otpctl_by_cd(db: AsyncSession, cd: str, value: str, updated_at: datetime) -> Any:
    result = await db.execute(update(otpctl_model).values(value=value, updated_at=updated_at).filter(otpctl_model.cd == cd))
    await db.commit()
    return result