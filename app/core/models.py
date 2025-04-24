from sqlalchemy import Column, Integer, Date, String
from app.core.database import Base

class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    currency = Column(String)
    value = Column(String)