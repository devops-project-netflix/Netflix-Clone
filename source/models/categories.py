import os
import sys
from db import connect_to_database
from bson.objectid import ObjectId
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db = connect_to_database('movies-db')
# Setting the value for category object id
SAMPLE_OBJECT_CAT = '5f716d75cffb4d9a4a5f8708'


class CategoriesModel:
    def __init__(self):
        self.collection = db.categories

    def get(self, query_params):
        movies = self.collection.find(query_params)
        return movies

    def getById(self, identifier):
        movies = self.collection.find_one({"_id": ObjectId(identifier)})
        return movies

    def update(self, identifier, movie):
        movies = self.collection.update({"_id": ObjectId(identifier)}, movie)
        return movies

    def insert(self, movie):
        movies = self.collection.insert_one(movie)
        return movies

    def delete(self, identifier):
        movies = self.collection.delete_one({"_id": ObjectId(identifier)})
        return movies
