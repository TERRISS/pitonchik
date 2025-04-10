from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

#TODO: вынеси в .env
#load_dotenv()
#
## Вынесите строку подключения в .env
#DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgresql:123@localhost:5430/testiki')
#
#engine = create_engine(DATABASE_URL)
#Base = declarative_base()
#
#Base.metadata.create_all(engine)
#Session = sessionmaker(bind=engine)
#session = Session()

#TODO : сделать схему
#TODO: install alembic (почитать что это)
#TODO: alembic update head