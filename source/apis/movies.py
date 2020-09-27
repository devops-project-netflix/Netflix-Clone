from flask import Flask, request
from flask_restx import Resource, Api, fields, marshal_with, reqparse, Namespace
import json
from db import *
from bson import json_util
from models.movies import MoviesModel
from seeds.seeder import database_seed

api = Namespace('Movies', description='all movies endpoints')

parser = api.parser()
parser.add_argument('name', type=str, help='movie name', location='param')
parser.add_argument('category', type=str, help='movie category', location='param')
parser.add_argument('tags', type=str, help='movie tags', location='param')

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
@api.route('/api/movies',endpoint='/api/movies')
class Movies(Resource):
	@api.expect(parser)
	def get(self):
		movies = MoviesModel().get({})
		movies_dict = [doc for doc in movies]
		movies_json_string = json.dumps(movies_dict, default=json_util.default)
		return json.loads(movies_json_string)

	@api.expect(movie)	
	def post(self):
		movie = request.get_json()
		code = MoviesModel().insert(movie)
		return "Successful insertion"

# 1. Standardize the REST in movies
# 2. Add the categories REST 
# 3. Check for better swagger
# 4. Environment file for flask
# 5. Standard requests and response