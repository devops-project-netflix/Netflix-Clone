import os
import sys
from models.movies import MoviesModel
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class MoviesSeed:
    def __init__(self):
        cwd = os.getcwd()
        self.seed_file = cwd + '/seeds/data/movies.json'

    def seed(self):
        print("Movie seed ..")
        with open(self.seed_file) as json_file:
            data = json.load(json_file)
            for index in range(len(data)):
                movie = MoviesModel().get({'Title': data[index]['Title']})
                movie = [doc for doc in movie]
                if(0 == len(movie)):
                    MoviesModel().insert(data[index])
