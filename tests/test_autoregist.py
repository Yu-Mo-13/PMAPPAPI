import pytest
from fastapi.testclient import TestClient
from main import app
from database.database import get_db, async_session
from models.autoregist import Autoregist as autoregist_model
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
import uuid

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
    new_autoregist = autoregist_model(
        uuid=uuid.uuid4(),
        pwd="test_pwd",
        app="test_app",
        other_info="test_info",
        registered_date=datetime.now()
    )
    db_session.add(new_autoregist)
    await db_session.commit()

    yield

    # Cleanup test data
    await db_session.execute(select(autoregist_model).filter(autoregist_model.app == "test_app").delete())
    await db_session.commit()

def test_get_all_autoregist(setup_test_data):
    response = client.get("/autoregist/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_autoregist_by_uuid(setup_test_data):
    response = client.get(f"/autoregist/uuid={setup_test_data.uuid}")
    assert response.status_code == 200
    assert response.json()["app"] == "test_app"

def test_create_autoregist(db_session: AsyncSession):
    response = client.post("/autoregist/create", params={"pwd": "new_pwd", "app": "new_app", "other_info": "new_info"})
    assert response.status_code == 200
    assert response.json()["app"] == "new_app"

    # Cleanup
    await db_session.execute(select(autoregist_model).filter(autoregist_model.app == "new_app").delete())
    await db_session.commit()

def test_delete_autoregist(db_session: AsyncSession):
    # Create autoregist to delete
    new_autoregist = autoregist_model(
        uuid=uuid.uuid4(),
        pwd="delete_pwd",
        app="delete_app",
        other_info="delete_info",
        registered_date=datetime.now()
    )
    db_session.add(new_autoregist)
    await db_session.commit()

    response = client.post(f"/autoregist/delete/uuid={new_autoregist.uuid}")
    assert response.status_code == 200

    # Verify deletion
    result = await db_session.execute(select(autoregist_model).filter(autoregist_model.uuid == new_autoregist.uuid))
    assert result.first() is None
