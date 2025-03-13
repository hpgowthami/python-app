from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.utils.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()