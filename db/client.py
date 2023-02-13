from pymongo import MongoClient
from config import DB_URL, DB_NAME

# Base de datos remota MongoDB
db_client = MongoClient(DB_URL)[DB_NAME]
