from flask import Flask, request
from flask_restx import Resource, Api, fields, marshal_with, reqparse, Namespace
import json
from db import *
from bson import json_util
from models.movies import MoviesModel
from utilities.responses import *
import itertools

api = Namespace('Tags', description='all movies tag endpoints')

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
@api.route('/api/movies')
class Movies(Resource):
	@api.expect(parser)
	@api.doc(responses={200: 'Movies List'})
	def get(self):
		#get all tags for all movies in DB
		tags = []
		movies = MoviesModel().get({})
		movies_dict = [doc for doc in movies]
		tempList = [mov['Tags'] for mov in movies_dict]
		flatList = list(set(itertools.chain(*tempList)))
		return http_response(200, flatList)
