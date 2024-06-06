from dotenv import load_dotenv
import os
from neo4j import GraphDatabase

# Load environment variables from .env file
load_dotenv()

# Retrieve variables from .env
AURA_CONNECTION_URI = os.getenv("AURA_CONNECTION_URI")
AURA_USERNAME = os.getenv("AURA_USERNAME")
AURA_PASSWORD = os.getenv("AURA_PASSWORD")

# Driver instantiation
driver = GraphDatabase.driver(
    AURA_CONNECTION_URI,
    auth=(AURA_USERNAME, AURA_PASSWORD)
)

