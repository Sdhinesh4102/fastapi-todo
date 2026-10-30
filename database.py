from sqlalchemy import create_engine
from sqlalchemy.engine import make_url
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL must be set in the environment or .env file")

database_url = make_url(DATABASE_URL)
if database_url.drivername == "postgresql":
    database_url = database_url.set(drivername="postgresql+psycopg2")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autoflush=False, bind=engine)
Base = declarative_base()