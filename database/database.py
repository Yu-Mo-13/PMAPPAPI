from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# config.pyから読み込む
from config import get_config

# SQLALCHEMY_DATABASE_URLでPOSTGRESの接続先を指定
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://" + get_config("PSUSER") + ":" + get_config("PSPASSWORD") + "@" + get_config("PSHOST") + ":" + get_config("PSPORT") + "/" + get_config("PSNAME")

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session