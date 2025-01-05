import pytest
from fastapi.testclient import TestClient
from main import app
from database.database import get_db, async_session
from models.otpctl import OtpCtl as otpctl_model
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
    new_otpctl = otpctl_model(
        cd="01",
        name="test_name",
        value="test_value",
        remarks="test_remarks",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db_session.add(new_otpctl)
    await db_session.commit()

    yield

    # Cleanup test data
    await db_session.execute(select(otpctl_model).filter(otpctl_model.cd == "01").delete())
    await db_session.commit()

def test_get_all_otpctl(setup_test_data):
    response = client.get("/otpctl")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_otpctl_value_by_cd(setup_test_data):
    response = client.get("/otpctl/cd=01")
    assert response.status_code == 200
    assert response.json()["cd"] == "01"

async def test_update_otpctl_by_cd(db_session: AsyncSession):
    response = client.put("/otpctl/cd=01", json={"value": "new_value"})
    assert response.status_code == 200
    assert response.json()["value"] == "new_value"

    # Cleanup
    await db_session.execute(select(otpctl_model).filter(otpctl_model.cd == "01").update({"value": "test_value"}))
    await db_session.commit()
