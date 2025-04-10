import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("POSTGRE_URL")

# Создание движка подключения
engine = create_engine(DATABASE_URL, echo=True)

# Базовый класс для моделей
Base = declarative_base()

from app.core.models import Currency

# Создание таблиц (если их нет)
Base.metadata.create_all(engine)


# Создание фабрики сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Получение сессии (вручную)
db_session = SessionLocal()

# TODO : сделать схему
# TODO: install alembic (почитать что это)
# TODO: alembic update head
