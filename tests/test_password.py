import pytest
from fastapi.testclient import TestClient
from main import app
from database.database import get_db, async_session
from models.password import Password as password_model
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
    new_password = password_model(
        pwd="test_password",
        app="test_app",
        other_info="test_info",
        registered_date=datetime.now()
    )
    db_session.add(new_password)
    await db_session.commit()

    yield

    # Cleanup test data
    await db_session.execute(select(password_model).filter(password_model.app == "test_app").filter(password_model.other_info == "test_info").delete())
    await db_session.commit()

def test_get_all_password(setup_test_data):
    response = client.get("/password/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_password_no_account(setup_test_data):
    response = client.get("/password/app=test_app")
    assert response.status_code == 200
    assert response.json()["app"] == "test_app"

def test_get_password(setup_test_data):
    response = client.get("/password/app=test_app/account=test_info")
    assert response.status_code == 200
    assert response.json()["app"] == "test_app"
    assert response.json()["other_info"] == "test_info"

async def test_create_password(db_session: AsyncSession):
    response = client.post("/password/create", json={"pwd": "new_password", "app": "new_app", "other_info": "new_info"})
    assert response.status_code == 200
    assert response.json()["app"] == "new_app"

    # Cleanup
    await db_session.execute(select(password_model).filter(password_model.app == "new_app").filter(password_model.other_info == "new_info").delete())
    await db_session.commit()
