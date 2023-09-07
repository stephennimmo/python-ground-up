from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from python_ground_up.settings import settings

engine = create_engine(settings.db_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
