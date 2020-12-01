import os
import sys
from db import connect_to_database
from bson.objectid import ObjectId

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

db = connect_to_database("movies-db")

SAMPLE_CONTENT_OBJECT = {
    "content": "the-shawshank-redemption.mp4",
    "status": "PENDING",
    "bucket": "bucket",
    "dash-content": "t-s-r.mpd",
}

NUM_KEYS = 5


class ContentModel:
    def __init__(self):
        self.collection = db.content

    def get(self, query_params):
        content = self.collection.find(query_params)
        return content

    def getById(self, identifier):
        content = self.collection.find_one({"_id": ObjectId(identifier)})
        return content

    def update(self, identifier, movie):
        content = self.collection.update({"_id": ObjectId(identifier)}, movie)
        return content

    def insert(self, movie):
        content = self.collection.insert_one(movie)
        return content

    def delete(self, identifier):
        content = self.collection.delete_one({"_id": ObjectId(identifier)})
        return content

    def getByIdNew(self, identifier):
        content = self.collection.find_one({"id": identifier})
        return content
