# Configuration database (database URI, etc.)

# Import modules
from app.dbbase import Base
from app.models import Pokemon
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
from app.envconfig import construct_db_uri

# Declare DB URI, Engine, and SessionLocal
DATABASE_URL = construct_db_uri()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


# 1. Create tables from models
def init_db():
    print("Creating tables...\n")
    Base.metadata.create_all(bind=engine)
    print("Tables created.\n")


# 2. Insert Pokémon records into PostgreSQL
def save_pokemon_list(data):
  added_count = 0

  # Use try-except to handle potential errors during database operations
  try:
    # Check for existing Pokémon before adding new ones
    with SessionLocal() as session:
      # Loop through each Pokémon in the data
      for column in data:
        # Check if the Pokémon already exists by ID & Name
        existing = session.query(Pokemon).filter(
          (Pokemon.id == column.get('id')) |
          (func.lower(Pokemon.name) == column.get('name').lower()) 
        ).first()

        # If it exists, skip adding it
        if existing:
          print(f"⚠️ Pokémon with ID {column.get('id')} or name '{column.get('name')}' already exists. Skipping.")
          continue

        # If it doesn't exist, create a new Pokémon record
        pokemon = Pokemon(
            id=column.get('id'),
            name=column.get('name'),
            height=column.get('height'),
            weight=column.get('weight')
        )

        # Add the new Pokémon to the session
        session.add(pokemon)
        added_count += 1

      # Commit the session to save changes to the database
      session.commit()
      print(f"{added_count} new Pokémon added to the database.\n")

  # Handle any exceptions that occur during the database operations
  except Exception as e:
    print("Error saving data:", e)


# 3. Query and display stored Pokémon
def show_all_pokemon():
  # Query all Pokémon from the database
  print("Fetching all Pokémon from the database...\n")

  # Better session handling using context manager
  with SessionLocal() as session:
    # Fetch all Pokémon records
    pokemon = session.query(Pokemon).all()
    # Loop through each Pokémon and print its details
    for character in pokemon:
      print(f"RECORD #{character.id}: {character.name}")

