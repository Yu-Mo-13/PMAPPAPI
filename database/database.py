from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# config.pyから読み込む
from config import get_config

SQLALCHEMY_DATABASE_URL = "mysql+aiomysql://" + get_config("DATABASE", "USER") + ":" + get_config("DATABASE", "PASSWORD") + "@" + get_config("DATABASE", "HOST") + ":" + get_config("DATABASE", "PORT") + "/" + get_config("DATABASE", "NAME")

async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session = sessionmaker(autocommit=False, autoflush=False, bind=async_engine, class_=AsyncSession)
Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session