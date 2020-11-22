import os
import sys
from db import connect_to_database
from bson.objectid import ObjectId
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db = connect_to_database('movies-db')
# Setting values for use in movies test
NUM_KEYS = 5
SAMPLE_OBJECT_ID = '5f96309bcd22acd9d23ebbeb'
SAMPLE_MOVIE_OBJECT = {'Title': 'The Shawshank Redemption'}
MOVIE_OBJECT = {
    "Categories": [
      "Movie"
    ],
    "Description": "Testing the post method for movies api",
    "Storage": "Azure/Test",
    "Tags": [
      "Drama"
    ],
    "Title": "I am here to test",
    "cast": [
      "Varun",
      "Ammar",
      "Sujay"
    ]
  }


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

    def getByIdNew(self, identifier):
        movies = self.collection.find_one({"id": identifier})
        return movies

    def getMovieRegex(self, query):
        movies = self.collection.find({"Title": {'$regex':query}})
        return movies