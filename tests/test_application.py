import pytest
from fastapi.testclient import TestClient
from main import app
from database.database import get_db, async_session
from models.application import Application as application_model
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
    new_application = application_model(
        name="test_app",
        accountclas="A",
        noticeclas="1",
        markclas="M",
        autosize="Y",
        registered_date=datetime.now()
    )
    db_session.add(new_application)
    await db_session.commit()

    yield

    # Cleanup test data
    await db_session.execute(select(application_model).filter(application_model.name == "test_app").delete())
    await db_session.commit()

def test_get_all_application(setup_test_data):
    response = client.get("/application/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_application(setup_test_data):
    response = client.get("/application/search/app=test_app")
    assert response.status_code == 200
    assert response.json()["name"] == "test_app"

def test_get_accountclass(setup_test_data):
    response = client.get("/application/app=test_app")
    assert response.status_code == 200
    assert response.json()["accountclas"] == "A"

def test_get_notice_app_list(setup_test_data):
    response = client.get("/application/notice/")
    assert response.status_code == 200
    assert len(response.json()) > 0

async def test_create_application(db_session: AsyncSession):
    response = client.post("/application/create", params={"name": "new_app", "accountclass": "B", "noticeclass": "0", "markclass": "N", "autosize": "N"})
    assert response.status_code == 200
    assert response.json()["name"] == "new_app"

    # Cleanup
    await db_session.execute(select(application_model).filter(application_model.name == "new_app").delete())
    await db_session.commit()

async def test_update_application(db_session: AsyncSession):
    # Create application to update
    new_application = application_model(
        name="update_app",
        accountclas="C",
        noticeclas="0",
        markclas="O",
        autosize="N",
        registered_date=datetime.now()
    )
    db_session.add(new_application)
    await db_session.commit()

    response = client.post("/application/update", params={"no": new_application.no, "accountclass": "D", "noticeclass": "1", "markclass": "P", "autosize": "Y"})
    assert response.status_code == 200

    # Verify update
    result = await db_session.execute(select(application_model).filter(application_model.no == new_application.no))
    updated_application = result.first()
    assert updated_application.accountclas == "D"
    assert updated_application.noticeclas == "1"
    assert updated_application.markclas == "P"
    assert updated_application.autosize == "Y"

    # Cleanup
    await db_session.execute(select(application_model).filter(application_model.no == new_application.no).delete())
    await db_session.commit()
