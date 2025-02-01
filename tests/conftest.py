import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import async_session
from sqlalchemy.future import select
from models.account import Account as account_model
from models.application import Application as application_model
from models.autoregist import Autoregist as autoregist_model
from models.otpctl import OtpCtl as otpctl_model
from models.password import Password as password_model
from models.passwordwk import PasswordWk as passwordwk_model
from datetime import datetime
import uuid

@pytest.fixture(scope="module")
async def db_session():
    async with async_session() as session:
        yield session

@pytest.fixture(scope="module")
def anyio_backend():
    return 'asyncio'

@pytest.fixture(scope="module")
async def setup_test_data(db_session: AsyncSession):
    # Insert test data for account
    new_account = account_model(
        account="test_account",
        app="test_app",
        deleteflg="0",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db_session.add(new_account)

    # Insert test data for application
    new_application = application_model(
        name="test_app",
        accountclas="A",
        noticeclas="1",
        markclas="M",
        autosize="Y",
        registered_date=datetime.now()
    )
    db_session.add(new_application)

    # Insert test data for autoregist
    new_autoregist = autoregist_model(
        uuid=uuid.uuid4(),
        pwd="test_pwd",
        app="test_app",
        other_info="test_info",
        registered_date=datetime.now()
    )
    db_session.add(new_autoregist)

    # Insert test data for otpctl
    new_otpctl = otpctl_model(
        cd="01",
        name="test_name",
        value="test_value",
        remarks="test_remarks",
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db_session.add(new_otpctl)

    # Insert test data for password
    new_password = password_model(
        pwd="test_password",
        app="test_app",
        other_info="test_info",
        registered_date=datetime.now()
    )
    db_session.add(new_password)

    # Insert test data for passwordwk
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
    await db_session.execute(select(account_model).filter(account_model.account == "test_account").filter(account_model.app == "test_app").delete())
    await db_session.execute(select(application_model).filter(application_model.name == "test_app").delete())
    await db_session.execute(select(autoregist_model).filter(autoregist_model.app == "test_app").delete())
    await db_session.execute(select(otpctl_model).filter(otpctl_model.cd == "01").delete())
    await db_session.execute(select(password_model).filter(password_model.app == "test_app").filter(password_model.other_info == "test_info").delete())
    await db_session.execute(select(passwordwk_model).filter(passwordwk_model.app == "test_appwk").filter(passwordwk_model.other_info == "test_infowk").delete())
    await db_session.commit()
