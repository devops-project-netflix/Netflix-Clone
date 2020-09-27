from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://ammar:abcd123@cluster0.8f754.mongodb.net/movies-db?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('movies-db')
video = pymongo.collection.Collection(db, 'video-collection')


# to get all the movies from the data base
def getAllMovies():
    movies = db.collection.find()

    return movies


def getMovieByName(name):

    out = db.collection.find_one({"Title": name})

    return out


def updateMovieByName(movie, name):

    code = db.collection.update({"Title": name}, movie)

    return code


def deleteMovieByName(name):

    code = db.collection.delete_one({"Title": name})

    return code


def insertNewMovie(movie):
    code = db.collection.insert_one(movie)

    return code


def getMovieByCast(actor):

    output = db.collection.find_one({"cast": actor})

    return output
