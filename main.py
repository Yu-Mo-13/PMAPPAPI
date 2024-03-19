from fastapi import FastAPI
from routers.application import router as application_router
from routers.password import router as password_router
from routers.account import router as account_router
from routers.authority import router as authority_router
from routers.user import router as user_router
from routers.passwordwk import router as passwordwk_router
from starlette.middleware.cors import CORSMiddleware
# from stargql import GraphQL

# from database.database import db_session
# from schema.schema import schema

app = FastAPI()

# CORSエラーを回避するための設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

# app.add_route("/graphql", GraphQL(schema=schema, graphiql=True))

# @app.on_event("shutdown")
# def shutdown_event():
#     db_session.remove()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(application_router)
app.include_router(password_router)
app.include_router(account_router)
app.include_router(authority_router)
app.include_router(user_router)
app.include_router(passwordwk_router)