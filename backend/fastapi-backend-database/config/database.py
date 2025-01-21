import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

load_dotenv()

# uri = os.getenv('MONGODB_URI', "mongodb://localhost/")
# client = MongoClient(uri)
client = MongoClient("mongodb://localhost:27017/")


db = client.kyc_bnp
collection_name = db["kyc_details"]
