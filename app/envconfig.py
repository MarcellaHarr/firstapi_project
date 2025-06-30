# app/envconfig.py
"""
Initializes environment variables and constructs database URI.
This script does not handle API requests—instead, it prepares shared settings
for the rest of the application.
"""

# 1. Import modules
from dotenv import load_dotenv
import os

# 2. Load environment variables from both shared and secret files
load_dotenv(".env.shared")
load_dotenv(".env.secret", override=True)

# 3. Access environment variables
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME")

# 4. Helper function to build the database URI
def construct_db_uri():
    return f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 5. Optional test when run directly (prints the DB URI)
if __name__ == "__main__":
    print("Constructed Database URI:")
    print(construct_db_uri())