# SQLAlchemy models (tables) definitions

# Import modules
from sqlalchemy import Column, Integer, String
from app.dbbase import Base

# Create Pokemon model
class Pokemon(Base):
  __tablename__ = 'pokemon'

  # Define columns
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False)
  height = Column(Integer)
  weight = Column(Integer)

  # Set objects as readable strings
  def __repr__(self):
    return f"<Pokemon(id={self.id}, name='{self.name}', height={self.height}, weight={self.weight})>"
