from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from percefons.core import settings
from .models import BaseModel

engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)
LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


BaseModel.metadata.create_all(bind=engine)
