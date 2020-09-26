from flask import Flask, request, jsonify
from flask_restx import Resource, Api
import json
from utils import return_index, ret_index
#import db
from db import *
from bson import json_util


app = Flask(__name__)
api = Api(app)
f = open('movies.json',)
movies = json.load(f)



    

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
        movies_json_string = json.dumps(movies_dict,default=json_util.default)

        return json.loads(movies_json_string)
    def post(self):
        movie = request.get_json()
        # db.db.collection.insert_one(movie)
        code = insertNewMovie(movie)
        return "Successful insertion"


'''
 @route    PUT GET DELETE /movies/name 
 @desc     Fetch, update and delete a movie by name
 @access   Public
'''
# GET PUT and DELETE the movies based on the id parameter of the video
@api.route('/movies/<string:name>')
#@api.response(404, 'Name not found.')
class MovieByName(Resource):
    def get(self, name):
        
        # out = db.db.collection.find_one({"Title":name})
        out = getMovieByName(name)
        #print (out)
        if out is None:
            return "Movie by this name doesn't exist, Please try again", 404
        
        movies_json_string = json.dumps(out,default=json_util.default)

        return json.loads(movies_json_string)
    def put(self, name):
        
        movie = request.get_json()
        #print (movie)
        # db.db.collection.update({"Title":name}, movie)
        output = getMovieByName(name)
        status = 200
        if output is None:
            movie = "No Movie with this name exists"
            status = 404
        else:
            code = updateMovieByName(movie, name)
            movie = "Movie updated successfully"
        # movies[index] = movie
        # json.dump(movies, f)
        return movie, status
    def delete(self, name):
        
        # db.db.collection.delete_one({"Title":name})
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


'''
This part was using json stub as our data provider 
Now I have moved the data to Mongo DB Atlas
'''
# GET, PUT and DELETE on the basis of the name of the video
# @api.route('/movies/<string:name>')
# class MovieByName(Resource):
#     def get(self, name):
#         # f = open('movies.json',)
#         # movies = json.load(f)
#         out = [x for x in movies if x['Title'] == name]
#         print (out)


#         return jsonify(out)
#     def put(self, name):
#         # f = open('movies.json',)
#         # movies = json.load(f)
#         index = return_index(movies, name)
#         # for i in range(len(movies)):
#         #     if movies[i]['Title'] == name:
#         #         index = i
#         #         break
        
        
#         f = open('movies.json','w')

#         movie = request.get_json()
#         #print (movie)

#         movies[index] = movie
#         json.dump(movies, f)
#         return jsonify(movies[index])
#     def delete(self, movie_id):
#         index = return_index(movies, name)
#         movies.pop(index)
#         f = open('movies.json', 'w')
#         json.dump(movies, f)

#         return 'None'  

if __name__ == '__main__':
    app.run(debug=True)