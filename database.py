from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgresql:123@localhost:5430/testiki')
Base = declarative_base()

class Currency(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    currency = Column(String)
    value = Column(String)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()