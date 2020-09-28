import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import *

db = connect_to_database('movies-db')

class MoviesModel:
	def __init__(self):
		self.collection = db.movies
	
	def get(self,query_params):
		movies = self.collection.find(query_params)
		return movies

	def getById(self,identifier):
		movies = self.collection.find_one({"_id": ObjectId(identifier)})
		return movies

	def update(self,identifier,movie):
		movies = self.collection.update({"_id": ObjectId(identifier)}, movie)
		return movies

	def insert(self,movie):
		movies = self.collection.insert_one(movie)
		return movies
		
	def delete(self,identifier):
		movies = self.collection.delete_one({"_id": ObjectId(identifier)})
		return movies
