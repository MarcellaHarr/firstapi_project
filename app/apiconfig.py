# `apiconfig.py` Initializes and configures the API to fetch and display information 
# about Pokémon.
# This script uses the PokeAPI to retrieve data about Pokémon based on user input.

# 1. Import modules
import requests

# 2. Store base url to a variable
base_url = "https://pokeapi.co/api/v2/"

# 3. Create a function to get a type of pokemon
def get_pokemon_info(name):
  # 6. use one of the api url filters to get the pokemon info
  url = f"{base_url}/pokemon/{name}"

  try:
    # 7. pass in the url to the `get method` of requests module with the response object
    response = requests.get(url)

    # 8. Check the response status code
    print("\n", response, "\n") # printed <Response [200]> if successful

    # 9. include a verification check for the response
    if response.status_code == 200:
      # 10. use the json method to convert the response to a json object
      pokemon_data = response.json()
      # 11. return the pokemon data
      return pokemon_data
    # 12. if the response is not successful, print the status code
    else:
      print(f"Failed to retrieve data {response.status_code}")
    # 13. if the response is not successful, return None
      return None
  
  # 16. Exceptions for various request errors
  except requests.exceptions.Timeout:
     print("The request has timed out. Please try again later.")
  except requests.exceptions.ConnectionError:
     print("The connection has timed out. Please check your internet connection.")
  except requests.exceptions.RequestException as e:
     print(f"An undefined error has occurred: {e}")
  
  # 17. Another return but for the case of an exception
  return None

# 18. End of the script
