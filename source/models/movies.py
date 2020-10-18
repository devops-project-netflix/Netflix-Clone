import os
import sys
from db import connect_to_database
from bson.objectid import ObjectId
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db = connect_to_database('movies-db')
# Setting values for use in movies test
NUM_KEYS = 5
SAMPLE_OBJECT_ID = '5f716d74cffb4d9a4a5f8704'
SAMPLE_MOVIE_OBJECT = {'Title': 'The Shawshank Redemption'}


class MoviesModel:
    def __init__(self):
        self.collection = db.movies

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
