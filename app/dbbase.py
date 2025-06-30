# Shared module for database operations

# Import modules
from sqlalchemy.orm import declarative_base

# Base class to be inherited by all models
Base = declarative_base()
