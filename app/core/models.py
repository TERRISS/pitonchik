from sqlalchemy import Column, Integer, Date, String
from app.core.database import Base

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    NumCode = Column(String)
    CharCode = Column(String)
    Nominal = Column(String)
    Name = Column(String)
    Value =  Column(String)

