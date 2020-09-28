import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from db import *
import platform

db = connect_to_database('movies-db')

class MoviesSeed:
	def __init__(self):
		cwd = os.getcwd()
		if platform.system() == 'Windows':
			self.seed_file = cwd + '\\seeds\\data\\movies.json'
		else:
			print (platform.system())
			self.seed_file = cwd + '/seeds/data/movies.json'
		
	def seed(self):
		with open(self.seed_file) as json_file:
			data = json.load(json_file)
			#print(data)
			#print("movies-seeder")