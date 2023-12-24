from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME
from dotenv import load_dotenv
import os


load_dotenv()
Base = declarative_base()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")


############################################################
######################### USER TABLE #######################
############################################################


class USER(Base):
    __tablename__ = "USER"
    id = Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    uid = Column(VARCHAR(36), nullable=False)
    first_name = Column(VARCHAR(36), nullable=False)
    last_name = Column(VARCHAR(36), nullable=False)
    email = Column(VARCHAR(100), nullable=False)
    username = Column(VARCHAR(36), nullable=False)
    password = Column(VARCHAR(64), nullable=False)
    created_at = Column(DATETIME, nullable=False)


############################################################
##################### CONVERSATION TABLE ###################
############################################################
