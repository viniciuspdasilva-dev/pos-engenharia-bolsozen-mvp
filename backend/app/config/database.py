from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from dotenv import load_dotenv

import os

load_dotenv()

Base = declarative_base()

# Classe usada para habilitar a conexão com a base de dados
# e permitir o DI do FastAPI
class Database:
    _engine = create_engine(os.getenv("DATABASE_URL"))
    _SessionLocal = sessionmaker(bind=_engine)
    def __init__(self):
        self.db = self._SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    @classmethod
    def get_db(cls):
        db = cls()._SessionLocal()
        try:
            yield db
        finally:
            db.close()