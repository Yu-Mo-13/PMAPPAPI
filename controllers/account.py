from typing import Any, List, Tuple

from sqlalchemy import select, update, insert
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from models.account import Account as account_model
from datetime import datetime

# アカウントマスター一覧画面で使用
async def get_all_account(db: AsyncSession) -> List[Tuple[int, str, str, str, datetime, datetime]]:
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
async def get_account(db: AsyncSession, account: str, app: str) -> List[Tuple[int, str, str, str, datetime, datetime]]:
    result: Result = await db.execute(select(
        account_model.id,
        account_model.account,
        account_model.app,
        account_model.deleteflg,
        account_model.created_at,
        account_model.updated_at
    ).filter(account_model.account == account).filter(account_model.app == app))
    return result.first()

# アカウントマスター詳細画面にて、アカウント情報を登録する際に使用
# created_atに現在の日付を設定する
# updated_atに現在の日付を設定する
# deleteflgに0を設定する
async def create_account(db: AsyncSession, account: str, app: str, deleteflg: str, created_at: datetime) -> Any:
    result = await db.execute(insert(account_model).values(account=account, app=app, deleteflg=deleteflg, created_at=created_at, updated_at=created_at))
    await db.commit()
    return result

# アカウントマスター詳細画面にて、アカウント情報を削除する際に使用
# updated_atに現在の日付を設定する
# deleteflgに1を設定する
async def delete_account(db: AsyncSession, account: str, app: str, deleteflg: str, updated_at: datetime) -> Any:
    result: Result = await db.execute(select(
        account_model.id,
        account_model.account,
        account_model.app,
        account_model.deleteflg,
        account_model.created_at,
        account_model.updated_at
    ).filter(account_model.account == account).filter(account_model.app == app))
    account_record = result.first()
    await db.execute(update(account_model).where(account_model.id == account_record.id).values(deleteflg=deleteflg, updated_at=updated_at))
    await db.commit()
    return await db.execute(select(account_model).filter(account_model.id == account_record.id)).first()
