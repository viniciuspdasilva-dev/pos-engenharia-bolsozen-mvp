import os

from dotenv import load_dotenv
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
)
from sqlalchemy.orm import Session, declarative_base

load_dotenv()

Base = declarative_base()


# Classe usada para habilitar a conexão com a base de dados
# e permitir o DI do FastAPI
class Database:
    _engine = create_async_engine(os.getenv("DATABASE_URL"))
    _SessionLocal = async_sessionmaker(bind=_engine)

    async def get_db(self) -> Session:
        async with self._SessionLocal() as session:
            try:
                yield session
                await session.commit()
            except exc.SQLAlchemyError as e:
                await session.rollback()
                raise e
