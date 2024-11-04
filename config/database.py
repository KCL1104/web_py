from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
import os

MONGO_DETAILS = ""  # Replace with your MongoDB URI

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.sample_mflix  # Replace with your database name

# Collections
user_collection = database.get_collection("users")
# movie_collection = database.get_collection("movies")
# theater_collection = database.get_collection("theaters")
# embedded_movie_collection = database.get_collection("embedded_movies")
# session_collection = database.get_collection("sessions")
# comment_collection = database.get_collection("comment s")