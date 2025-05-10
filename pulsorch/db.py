from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from pulsorch import config


engine = create_engine(config.get_db_url())
db_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    Base.metadata.create_all(bind=engine)


class Base(DeclarativeBase):
    pass
