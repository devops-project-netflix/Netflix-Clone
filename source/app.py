from flask import Flask, request, jsonify
from flask_restx import Resource, Api
import json


app = Flask(__name__)
api = Api(app)
f = open('movies.json',)
movies = json.load(f)
# movies = [
#     {
#         "name": "The Shawshank Redemption",
#         "id": "1",
#         "cast": [
#             "Tim Robbins",
#             "Morgan Freeman",
#             "Bob Gunton",
#             "William Sadler"
#         ],
#         "genres": [
#             "Drama"
#         ]
#     },
#     {
#         "name": "The Godfather",
#         "id": "2",
#         "cast": [
#             "Marlon Brando",
#             "Al Pacino",
#             "James Caan",
#             "Diane Keaton"
#         ],
#         "genres": [
#             "Crime",
#             "Drama"
#         ]
#     }
# ]



@api.route('/movies')
class AllMovies(Resource):
    def get(self):
        return jsonify(movies)

@api.route('/movies/<string:movie_id>')
class MovieById(Resource):
    def get(self, movie_id):
        out = [x for x in movies if x['id'] == movie_id]
        print (out)


        return jsonify(out)
    

if __name__ == '__main__':
    app.run(debug=True)