from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#TODO: вынеси в .env
engine = create_engine('postgresql://postgresql:123@localhost:5430/testiki')
Base = declarative_base()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

#TODO : сделать схему
#TODO: install alembic (почитать что это)
#TODO: alembic update head