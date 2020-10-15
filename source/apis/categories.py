from flask import request
from flask_restx import Resource, fields, Namespace
from models.categories import CategoriesModel
from utilities.responses import http_response
from utilities.errors import errors

api = Namespace('Categories', description='all video categories endpoints')

parser = api.parser()
parser.add_argument('name', type=str, help='category name', location='param')


category = api.model('Category', {
    'Name': fields.String,
    'Description': fields.String,
})

# Getting the list of all videos and adding new video
'''
 @route    POST api/categories and GET api/categories
 @desc     Add a movie and fetch all the movies from DB
 @access   Public
'''


@api.route('/api/categories')
class Categories(Resource):
    @api.expect(parser)
    @api.doc(responses={200: 'Categories List'})
    def get(self):
        categories = CategoriesModel().get({})
        categories = [doc for doc in categories]
        return http_response(200, categories)

    @api.expect(category)
    @api.doc(responses={201: 'Category Inserted'})
    def post(self):
        category = request.get_json()
        code = CategoriesModel().insert(category)
        return http_response(201, {"status": "category record inserted"})


'''
 @route    PUT GET DELETE /api/categories/<string:objectId>
 @desc     Fetch, update and delete a movie by id
 @access   Public
'''


@api.route('/api/categories/<string:objectId>')
class CategoriesById(Resource):
    @api.doc(responses={200: 'A category doc'})
    def get(self, objectId):
        category = CategoriesModel().getById(objectId)
        if category is not None:
            return http_response(200, category)
        else:
            return errors['MovieNotExistsError'], errors['MovieNotExistsError']['status']


    @api.expect(category)
    @api.doc(responses={202: 'Movie Updated'})
    def put(self, objectId):
        category = request.get_json()
        code = CategoriesModel().update(objectId, category)
        print (code)
        if code['nModified'] != 0:
            return http_response(202, {"status": "category record updated"})
        else:
            return errors['UpdatingMovieError'], errors['UpdatingMovieError']['status']


    @api.doc(responses={204: 'Movie Deleted'})
    def delete(self, objectId):
        category = CategoriesModel().delete(objectId)
        return http_response(204, {"status": "category record deleted"})
