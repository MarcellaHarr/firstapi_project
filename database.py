# Configuration database (database URI, etc.)

# Import modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Pokemon
from app.envconfig import construct_db_uri

DATABASE_URL = construct_db_uri()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


# 1. Create tables from models
def init_db():
    print("Creating tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")


# 2. Insert Pokémon records into PostgreSQL
def save_pokemon_list(data):
  session = SessionLocal()
  added_count = 0

  # Check if the table exists, if not, create it
  try:
    for column in data:
      existing = session.query(Pokemon).filter_by(id=column.get('id')).first()
      if existing:
        print(f"⚠️ Pokémon ID {column.get('id')} ({column.get('name')}) already exists. Skipping.")
        continue

      pokemon = Pokemon(
          id = column.get('id'),
          name = column.get('name'),
          height = column.get('height'),
          weight = column.get('weight')
      )
      session.add(pokemon)
      added_count += 1

    session.commit()
    print(f"{added_count} new Pokémon added to the database.")

  # Handle any exceptions that occur during the transaction
  except Exception as e:
    session.rollback()
    print("Error saving data:", e)

  # Ensure the session is closed
  finally:
    session.close()


# 5. Query and display stored Pokémon
def show_all_pokemon():
  # Create a new session
  session = SessionLocal()

  # Query all Pokémon records
  try:
    pokemon = session.query(Pokemon).all()
    for character in pokemon:
      print(f"RECORD #{character.id}: {character.name}")
  finally:
    session.close()

