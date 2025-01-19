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