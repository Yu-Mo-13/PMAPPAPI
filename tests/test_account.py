import pytest
from fastapi.testclient import TestClient
from main import app
from database.database import get_db, async_session
from models.account import Account as account_model
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime

client = TestClient(app)

@pytest.fixture(scope="module")
async def db_session():
    async with async_session() as session:
        yield session

@pytest.fixture(scope="module")
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope="module")
async def setup_test_data(db_session: AsyncSession):
    # Insert test data
    new_account = account_model(
        account="test_account",
        app="test_app",
        deleteflg="0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db_session.add(new_account)
    await db_session.commit()

    yield

    # Cleanup test data
    await db_session.execute(select(account_model).filter(account_model.account == "test_account").filter(account_model.app == "test_app").delete())
    await db_session.commit()

def test_get_all_account(setup_test_data):
    response = client.get("/account/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_all_account_by_appname(setup_test_data):
    response = client.get("/account/app=test_app")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_account(setup_test_data):
    response = client.get("/account/app=test_app/account=test_account")
    assert response.status_code == 200
    assert response.json()["account"] == "test_account"

async def test_create_account(db_session: AsyncSession):
    response = client.post("/account/create/app=new_app/account=new_account")
    assert response.status_code == 200
    assert response.json()["account"] == "new_account"

    # Cleanup
    await db_session.execute(select(account_model).filter(account_model.account == "new_account").filter(account_model.app == "new_app").delete())
    await db_session.commit()

async def test_delete_account(db_session: AsyncSession):
    # Create account to delete
    new_account = account_model(
        account="delete_account",
        app="delete_app",
        deleteflg="0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db_session.add(new_account)
    await db_session.commit()

    response = client.post("/account/delete/app=delete_app/account=delete_account")
    assert response.status_code == 200

    # Verify deletion
    result = await db_session.execute(select(account_model).filter(account_model.account == "delete_account").filter(account_model.app == "delete_app"))
    assert result.first() is None
