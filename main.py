from fastapi import FastAPI
from stargql import GraphQL

from database.database import db_session
from schema.schema import schema

app = FastAPI()

app.add_route("/graphql", GraphQL(schema=schema, graphiql=True))

@app.on_event("shutdown")
def shutdown_event():
    db_session.remove()