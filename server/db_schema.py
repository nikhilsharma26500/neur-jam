from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME, BOOLEAN, TEXT
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()
Base = declarative_base()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))


############################################################
######################### USER TABLE #######################
############################################################


class USER(Base):
    __tablename__ = "users"
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    uid = Column(VARCHAR(32), primary_key=True, unique=True, nullable=False)
    first_name = Column(VARCHAR(36), nullable=False)
    last_name = Column(VARCHAR(36), nullable=False)
    email = Column(VARCHAR(100), unique=True, nullable=False)
    username = Column(VARCHAR(36), unique=True, nullable=False)
    password_hash = Column(VARCHAR(64), unique=True, nullable=False)
    is_active = Column(BOOLEAN, default=True, nullable=False)
    is_verified = Column(BOOLEAN, default=False, nullable=False)
    last_login = Column(DATETIME, nullable=False)
    created_at = Column(DATETIME, nullable=False)


############################################################
##################### CONVERSATION TABLE ###################
############################################################


class CONVERSATION(Base):
    __tablename__ = "conversations"
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    uid = Column(VARCHAR(36), ForeignKey("users.uid"), nullable=False)
    chat_id = Column(VARCHAR(36), unique=True, nullable=False)
    model = Column(VARCHAR(36), nullable=False)
    user_query = Column(VARCHAR(4000), nullable=False)
    model_reponse = Column(TEXT, nullable=False)
    created_at = Column(DATETIME, nullable=False)


############################################################
##################### DATABASE CONNECTION ##################
############################################################


SQLALCHEMY_DATABASE_URL = (
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

connect_args = {"raise_on_warnings": False}

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)
Base.metadata.create_all(bind=engine)

table_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
