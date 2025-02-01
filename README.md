# PMAPP API
## Description
PMAPPで使用するAPIです。

# 環境構築
## 使用パッケージ
・fastapi
・uvicorn
・sqlalchemy
・aiomysql
・pydantic
・datetime

# アプリケーション起動
```
uvicorn main:app --reload
```

# Unit Test Setup
## Install necessary libraries
```bash
pip install fastapi
pip install uvicorn
pip install sqlalchemy
pip install aiomysql
pip install pydantic
pip install datetime
pip install asyncpg
pip install pytest
```

## Run Unit Tests
```bash
pytest
```

## Run Specific Unit Test File
```bash
pytest tests/test_account.py
```

# Alembic初期化
```
alembic init alembic
```

# マイグレーションファイル自動生成
```
alembic revision --autogenerate -m "create xxx table"
```

# マイグレーションファイル実行
```
alembic upgrade head
```

# マイグレーションファイル実行(既にテーブルが存在する場合)
```
alembic revision -m "create xxx table"
```
