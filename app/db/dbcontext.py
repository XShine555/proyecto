from os import getenv
from sqlmodel import SQLModel, create_engine, Session

__database_url = getenv("DATABASE_URL")
__engine = create_engine(__database_url, echo=True)

def init_db():
    SQLModel.metadata.create_all(__engine)

def get_session():
    session = Session(__engine)
    try:
        yield session
    finally:
        session.close()