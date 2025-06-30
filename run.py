# This script is used to run the application by importing the main 
# function from the apiconfig
"""
Entry point to launch the application.
It fetches a Pokémon via user input, saves it to PostgreSQL, and displays all stored Pokémon.
"""

# Import main controller logic from the app
from app.routes.api_views import fetch_and_store_pokemon
from database import init_db

# Check to run the app directly
if __name__ == '__main__': 
  # Initialize the database
  init_db()

  # Keep the app running until the user decides to exit
  print("Welcome to the Pokémon Database!\n")
  while True:
    user_input = input("Enter the name of a Pokémon (or type 'exit' to quit): ").strip().lower()
    if user_input == "exit":
      print("Goodbye! 👋")
      break
    if not user_input:
      print("No Pokémon name provided.\n")
      continue

    # Handle the input and fetch Pokémon data
    fetch_and_store_pokemon(user_input)
