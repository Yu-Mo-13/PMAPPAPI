from fastapi import FastAPI
from routers.application import router as application_router
from routers.password import router as password_router
# from stargql import GraphQL

# from database.database import db_session
# from schema.schema import schema

app = FastAPI()

# app.add_route("/graphql", GraphQL(schema=schema, graphiql=True))

# @app.on_event("shutdown")
# def shutdown_event():
#     db_session.remove()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(application_router)
app.include_router(password_router)