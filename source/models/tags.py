import os
import sys
from db import connect_to_database
from bson.objectid import ObjectId
import itertools
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db = connect_to_database('movies-db')

# setting  values to be used for testing
SAMPLE_OBJECT_ARRAY = ['5f967b0cda579d10e010ecac', '5f96309bcd22acd9d23ebbeb']
TAGS_ARRAY = ['Drama', 'NotFound']
HTML_OK = "200 OK"
MOVIE = "Movie"
MOVIE_LENGTH = 1
MOVIE_NOTFOUND = 0


class TagsModel:
    def __init__(self):
        self.collection = db.movies

    def get(self, query_params):
        movies = self.collection.find(query_params)
        return movies

    def getByTag(self, identifier):
        movies = self.collection.find()
        result = []
        movies_dict = [doc for doc in movies]
        for mov in movies_dict:
            if ''.join(identifier).lower() in map(str.lower, mov['Tags']):
                result.append(mov)
        return result

    def getRecommendations(self, watched):
        recommendations = []
        categories = []
        descriptions = []
        title = []
        cast = []
        tags = []
        for i in watched:
            movies = self.collection.find_one({"_id": ObjectId(i)})
            print(movies)
            categories.append(movies['Categories'])
            descriptions.append(movies['Description'])
            title.append(movies['Title'])
            cast.append(movies['cast'])
            tags.append(movies['Tags'])

        categories = list(set(itertools.chain(*categories)))
        descriptions = list(set(itertools.chain(*descriptions)))
        title = list(set(itertools.chain(*title)))
        cast = list(set(itertools.chain(*cast)))
        tags = list(set(itertools.chain(*tags)))

        movies = self.collection.find()

        for mov in movies:
            if set(categories).intersection(set(mov['Categories'])) != 0:
                recommendations.append(mov)
            elif len(descriptions) >= len(mov['Description']):
                recommendations.append(mov)
            elif len(max(title)) >= len(mov['Title']):
                recommendations.append(mov)
            elif set(cast).intersection(set(mov['cast'])) != 0:
                recommendations.append(mov)
            elif set(tags).intersection(set(mov['Tags'])) != 0:
                recommendations.append(mov)
        return recommendations

    def update(self, identifier, movie):
        movies = self.collection.update({"_id": ObjectId(identifier)}, movie)
        return movies

    def insert(self, movie):
        movies = self.collection.insert_one(movie)
        return movies

    def delete(self, identifier):
        movies = self.collection.delete_one({"_id": ObjectId(identifier)})
        return movies
