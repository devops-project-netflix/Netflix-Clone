from flask import request
from flask_restx import Resource, fields, Namespace
from models.movies import MoviesModel
from models.tags import TagsModel
from utilities.responses import http_response
import itertools

api = Namespace('Tags', description='all movies tag endpoints')

parser = api.parser()
parser.add_argument('id', type=list, help='ID', location='param')

movie = api.model('Movie', {
    'Title': fields.String,
    'Description': fields.String,
    'Categories': fields.List(fields.String),
    'Tags': fields.List(fields.String),
    'Cast': fields.List(fields.String),
})


@api.route('/api/tags')
class Movies(Resource):
    @api.expect(parser)
    @api.doc(responses={200: 'Movies List'})
    def get(self):
        # get all tags for all movies in DB
        tags = []
        movies = MoviesModel().get({})
        movies_dict = [doc for doc in movies]
        tempList = [mov['Tags'] for mov in movies_dict]
        flatList = list(set(itertools.chain(*tempList)))
        return http_response(200, flatList)

# Getting the list of the tags of all the videos in the database


'''
 @route    GET /tags
 @desc     Get all the movie tags for all movies
 @access   Public
'''


@api.route('/api/tags/<string:objectTag>')
class MoviebyTag(Resource):
    @api.doc(responses={200: 'A category doc'})
    def get(self, objectTag):
        movies = TagsModel().getByTag({objectTag})
        if not movies:
            movies = "No results found"
            return http_response(200, movies)
        return http_response(200, movies)


@api.route('/api/TagRecommend/')
class RecommendbyTag(Resource):
    @api.expect(parser)
    @api.doc(responses={200: 'Found Recommendations'})
    def get(self):
        inp = request.args.get('id')
        watched = inp.split(",")
        movies = TagsModel().getRecommendations(watched)
        return http_response(200, movies)


@api.expect(movie)
@api.route('/api/tags/<string:objectId>')
class UpdateMovieTags(Resource):
    @api.doc(responses={202: 'Movie Updated'})
    def put(self, objectId):
        category = request.get_json()
        print(category)
        code = TagsModel().update(objectId, category)
        return http_response(202, {"status": "category record updated"})
