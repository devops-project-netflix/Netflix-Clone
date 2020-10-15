from flask import request
from flask_restx import Resource, fields, Namespace
from models.movies import MoviesModel
from utilities.responses import http_response
from pymongo.errors import OperationFailure
from utilities.errors import errors

api = Namespace('Movies', description='all movies endpoints')

parser = api.parser()
parser.add_argument('Title', type=str, help='movie name', location='param')
parser.add_argument('Categories', type=str, help='movie category', location='param')
parser.add_argument('Tags', type=str, help='movie tags', location='param')

movie = api.model('Movie', {
    'Title': fields.String,
    'Description': fields.String,
    'Categories': fields.List(fields.String),
    'Tags': fields.List(fields.String),
    'Cast': fields.List(fields.String),
})


# Getting the list of all videos and adding new video
'''
 @route    POST /movies and GET /movies
 @desc     Add a movie and fetch all the movies from DB
 @access   Public
'''


@api.route('/api/movies')
class Movies(Resource):
    @api.expect(parser)
    @api.doc(responses={200: 'Movies List'})
    def get(self):
        query_params = request.args.to_dict()
        movies = MoviesModel().get(query_params)
        movies_dict = [doc for doc in movies]
        return http_response(200, movies_dict)

    @api.expect(movie)
    @api.doc(responses={201: 'Movie Inserted'})
    def post(self):
        movie = request.get_json()
        code = MoviesModel().insert(movie)
        return http_response(201, {"status": "movie record inserted"})


'''
 @route    PUT GET DELETE /movies/id
 @desc     Fetch, update and delete a movie by id
 @access   Public
'''


@api.route('/api/movies/<string:objectId>')
class MoviesById(Resource):
    @api.doc(responses={200: 'A movie doc'})
    def get(self, objectId):
            movie = MoviesModel().getById(objectId)
            if movie is not None:
                return http_response(200, movie)
            else:
                return errors['MovieNotExistsError'], errors['MovieNotExistsError']['status']

    @api.expect(movie)
    @api.doc(responses={202: 'Movie Updated'})	
    def put(self, objectId):
        movie = request.get_json()
        code = MoviesModel().update(objectId, movie)
        if code['nModified'] != 0:
            return http_response(202, {"status": "movie record updated"})
        else:
            return errors['UpdatingMovieError'], errors['UpdatingMovieError']['status']


    @api.doc(responses={204: 'Movie Deleted'})
    def delete(self, objectId):
        movie = MoviesModel().delete(objectId)
        print (movie)
        return http_response(204, {"status": "movie record deleted"})


# 1. Standardize the REST in movies
# 2. Add the categories REST
# 3. Check for better swagger
# 4. Environment file for flask
# 5. Standard requests and response
