import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import *
from bson.objectid import ObjectId


db = connect_to_database('movies-db')

class TagsModel:
	def __init__(self):
		self.collection = db.movies
	
	def get(self,query_params):
		movies = self.collection.find(query_params)
		return movies

	def getByTag(self,identifier):
		movies = self.collection.find()
		result = []
		movies_dict = [doc for doc in movies]
		for mov in movies_dict:
			if ''.join(identifier).lower() in map(str.lower, mov['Tags']):
				result.append(mov)
		return result

	def update(self,identifier,movie):
		movies = self.collection.update({"_id": ObjectId(identifier)}, movie)
		return movies

	def insert(self,movie):
		movies = self.collection.insert_one(movie)
		return movies
	def delete(self,identifier):
		movies = self.collection.delete_one({"_id": ObjectId(identifier)})
		return movies
