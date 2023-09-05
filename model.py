from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

client = MongoClient(os.getenv('MongoDB_URL'))  # MongoDB URL
db = client[os.getenv("db")]  # database name
collection = db[os.getenv("collection")]  # collection name
