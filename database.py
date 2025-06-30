# Configuration database (database URI, etc.)

# Import modules
# from sqlalchemy.ext.declarative import declarative_base (older way)
from sqlalchemy.orm import sessionmaker, declarative_base
from app.envconfig import construct_db_uri
from sqlalchemy import create_engine

# Create the engine using your helper function, and set up the base class for models
DATABASE_URL = construct_db_uri()
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

