import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")

if not MONGODB_URL:
    raise ValueError("MONGODB_URL no se encontro")

client = MongoClient(
    MONGODB_URL,
    server_api = ServerApi("1"),
    serverSelectionTimeoutMS = 5000
)

database = client["user_management"]

users_collection = database["users"]

if __name__ == "__main__":
    try:
        client.admin.command("ping")
        print("Coneccion con Atlas Estable")
    
    except Exception as error:
        print(f"Error De Coneccion a Mongo: {error}")