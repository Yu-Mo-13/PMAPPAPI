from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker)
# import pymysql
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://user01:user01@localhost:3306/password"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Password(Base):
    __tablename__ = "password"
    no = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pwd = Column(String(200), index=True)
    app = Column(String(200), index=True)
    email_address = Column(String(100), index=True)
    other_info = Column(String(100), index=True)
    firestoreRegFlg = Column(String(1), index=True)
    registered_date = Column(DateTime, default=datetime.now)

class Application(Base):
    __tablename__ = "application"
    no = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), index=True)
    accountClas = Column(String(1), index=True)
    registered_date = Column(DateTime, default=datetime.now)