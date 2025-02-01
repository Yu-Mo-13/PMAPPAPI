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
uvicorn main:app --reload

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
