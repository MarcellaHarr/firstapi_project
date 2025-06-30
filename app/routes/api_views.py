# Controls the logic for fetching Pokémon data, saving it, and 
# storing it in the PostgreSQL database.

# Import modules
from database import save_pokemon_list, show_all_pokemon
from app.apiconfig import get_pokemon_info

# Function to fetch Pokémon data from the PokeAPI and store it in the database
def fetch_and_store_pokemon():
  # Prompt the user for a Pokémon name
  print("Welcome to the Pokémon Database!\n")
  name = input("Enter the name of a Pokémon to store in the database: ").lower().strip()

  # Check if the name is provided
  if not name:
    print("No Pokémon name provided.")
    return

  # Fetch Pokémon data from the PokeAPI
  print(f"Fetching data for Pokémon: {name}...\n")
  pokemon_data = get_pokemon_info(name)

  # If data is found, print the details and save to the database
  if pokemon_data:
    print(f"Pokemon's Name: {pokemon_data['name'].capitalize()}")
    print(f"Pokemon's ID: {pokemon_data['id']}")
    print(f"Pokemon's Height: {pokemon_data['height']} decimetres.")
    print(f"Pokemon's Weight: {pokemon_data['weight']} hectograms.\n")

    # Prepare the payload for saving to the database
    payload = [{
        "id": pokemon_data["id"],
        "name": pokemon_data["name"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"]
    }]

    # Save the Pokémon data to the database
    print("Saving Pokémon data to the database...\n")
    save_pokemon_list(payload)

    # Show all Pokémon stored in the database
    show_all_pokemon()

  # If no data is found, print a message
  else:
        print("No data found for the specified Pokémon.")
