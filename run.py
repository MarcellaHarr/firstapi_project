# This script is used to run the application by importing the main 
# function from the apiconfig
"""
Entry point to launch the application.
It fetches a Pokémon via user input, saves it to PostgreSQL, and displays all stored Pokémon.
"""

# Import main controller logic from the app
from app.routes.api_views import fetch_and_store_pokemon

if __name__ == '__main__':
    fetch_and_store_pokemon()
