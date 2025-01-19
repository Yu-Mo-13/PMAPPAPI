# alembic/env.py

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from sqlalchemy import create_engine

# ここで FastAPI プロジェクトのパスを読み込み
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from database.database import Base
from database.database import async_engine

# マイグレーション対象のモデルをインポート
from models.menu import Menu

# Alembic Config オブジェクトを取得し
config = context.config

# もし alembic.ini に接続情報を直接書いている場合は以下が必要：
# config.set_main_option("sqlalchemy.url", "postgresql://user:password@localhost/db")

# ログ設定
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ターゲットとなるメタデータを指定
target_metadata = Base.metadata


def run_migrations_offline():
    """
    オフラインモードでのマイグレーション
    (DB 接続を行わずに SQL ファイルを出力するなど)
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, 
        target_metadata=target_metadata, 
        literal_binds=True, 
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    オンラインモードでのマイグレーション
    (実際に DB に接続してマイグレーションを実行)
    """
    # asyncpg URLをpsycopg2用に変換
    sync_url = str(async_engine.url).replace('postgresql+asyncpg', 'postgresql+psycopg2')
    connectable = create_engine(sync_url)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


# Alembic の実行パラメータを判定して、オンラインモードかオフラインモードかを選択
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
