from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, DATETIME
from dotenv import load_dotenv
import os


