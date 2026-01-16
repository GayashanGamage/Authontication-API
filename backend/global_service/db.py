from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

load_dotenv()


def get_database():
    uri = os.getenv('db')

    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Successfully connected to MongoDB!")
        return client.get_database("authentication")
    
    except Exception as e:
        print(e)
        return None
    print('transaction ended')