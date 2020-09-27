from flask import Flask, request
from flask_restx import Resource, Api
import json
from db import *
from bson import json_util


app = Flask(__name__)
api = Api(app)


# Getting the list of all videos and adding new video
'''
 @route    POST /movies and GET /movies
 @desc     Add a movie and fetch all the movies from DB
 @access   Public
'''


@api.route('/movies')
class AllMovies(Resource):
    def get(self):
        # f = open('movies.json',)
        # movies = json.load(f)
        # movies = db.db.collection.find()
        movies = getAllMovies()
        movies_dict = [doc for doc in movies]
        movies_json_string = json.dumps(movies_dict, default=json_util.default)

        return json.loads(movies_json_string)

    def post(self):
        movie = request.get_json()
        code = insertNewMovie(movie)
        return "Successful insertion"


'''
 @route    PUT GET DELETE /movies/name
 @desc     Fetch, update and delete a movie by name
 @access   Public
'''


# GET PUT and DELETE the movies based on the id parameter of the video
@api.route('/movies/<string:name>')
class MovieByName(Resource):
    def get(self, name):

        out = getMovieByName(name)
        print(out)
        if out is None:
            return "Movie by this name doesn't exist, Please try again", 404

        movies_json_string = json.dumps(out, default=json_util.default)

        return json.loads(movies_json_string)


    def put(self, name):
        
        movie = request.get_json()
        output = getMovieByName(name)
        status = 200
        if output is None:
            movie = "No Movie with this name exists"
            status = 404
        else:
            code = updateMovieByName(movie, name)
            movie = "Movie updated successfully"

        return movie, status


    def delete(self, name):
        
        out = getMovieByName(name)
        message = None
        status = 200
        if out is not None:
            code = deleteMovieByName(name)
            message = 'Successful deletion'
        else:
            message = 'No movie with this name exists in the DB'
            status = 404

        return message, status


# Getting the list of all videos and adding new video
'''
 @route    GET /movie/cast/name
 @desc     Fetch movie by name
 @access   Public
'''
# GET PUT and DELETE the movies based on the id parameter of the video


@api.route('/movie/cast/<string:name>')
class MovieByCast(Resource):
    def get(self, name):

        # out = db.db.collection.find_one({"Title":name})
        out = getMovieByCast(name)
        print(out)
        if out is None:
            return "Movie by this name doesn't exist, Please try again", 404

        movies_json_string = json.dumps(out, default=json_util.default)

        return json.loads(movies_json_string)


if __name__ == '__main__':
    app.run(debug=True)
