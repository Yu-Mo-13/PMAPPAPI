from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.account import Account as account_model

# アカウントマスター一覧画面で使用
async def get_all_account(db: AsyncSession) -> List[Tuple[int, str, str, str, str, str]]:
    result: Result = await db.execute(select(
        account_model.id,
        account_model.account,
        account_model.app,
        account_model.deleteflg,
        account_model.created_at,
        account_model.updated_at
    ).filter(account_model.deleteflg == '0'))
    return result.all()

# アカウントマスター詳細画面で使用
async def get_account(db: AsyncSession, account: str, app: str) -> List[Tuple[int, str, str, str, str, str]]:
    result: Result = await db.execute(select(
        account_model.id,
        account_model.account,
        account_model.app,
        account_model.deleteflg,
        account_model.created_at,
        account_model.updated_at
    ).filter(account_model.account == account).filter(account_model.app == app))
    return result.first()