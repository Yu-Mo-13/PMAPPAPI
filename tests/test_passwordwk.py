import pytest
from fastapi.testclient import TestClient
from main import app
from database.database import get_db, async_session
from models.passwordwk import PasswordWk as passwordwk_model
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
    new_passwordwk = passwordwk_model(
        pwd="test_passwordwk",
        app="test_appwk",
        other_info="test_infowk",
        registered_date=datetime.now()
    )
    db_session.add(new_passwordwk)
    await db_session.commit()

    yield

    # Cleanup test data
    await db_session.execute(select(passwordwk_model).filter(passwordwk_model.app == "test_appwk").filter(passwordwk_model.other_info == "test_infowk").delete())
    await db_session.commit()

def test_get_all_passwordwk(setup_test_data):
    response = client.get("/passwordwk/")
    assert response.status_code == 200
    assert len(response.json()) > 0

async def test_create_passwordwk(db_session: AsyncSession):
    response = client.post("/passwordwk/create", json={"pwd": "new_passwordwk", "app": "new_appwk", "other_info": "new_infowk"})
    assert response.status_code == 200
    assert response.json()["app"] == "new_appwk"

    # Cleanup
    await db_session.execute(select(passwordwk_model).filter(passwordwk_model.app == "new_appwk").filter(passwordwk_model.other_info == "new_infowk").delete())
    await db_session.commit()

def test_delete_passwordwk(setup_test_data):
    response = client.delete("/passwordwk/delete", json={"app": "test_appwk", "other_info": "test_infowk"})
    assert response.status_code == 200
    assert response.json()["app"] == "test_appwk"
    assert response.json()["other_info"] == "test_infowk"
