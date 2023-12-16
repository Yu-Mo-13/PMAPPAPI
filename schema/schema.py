import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType
from database.database import Password as PasswordModel, Application as ApplicationModel

class Password(SQLAlchemyObjectType):
    class Meta:
        model = PasswordModel
        interfaces = (relay.Node, )

class PasswordConnection(relay.Connection):
    class Meta:
        node = Password

class Application(SQLAlchemyObjectType):
    class Meta:
        model = ApplicationModel
        interfaces = (relay.Node, )

class ApplicationConnection(relay.Connection):
    class Meta:
        node = Application

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_passwords = SQLAlchemyConnectionField(PasswordConnection)
    all_applications = SQLAlchemyConnectionField(ApplicationConnection)

schema = graphene.Schema(query=Query)