import unittest

from flask_restx import Namespace
from models.movies import MoviesModel, NUM_KEYS, SAMPLE_OBJECT_ID, SAMPLE_MOVIE_OBJECT
from models.tags import TagsModel, HTML_OK, MOVIE_LENGTH, MOVIE_NOTFOUND

api = Namespace('Movies', description='all movies endpoints')

parser = api.parser()
parser.add_argument('Title', type=str, help='movie name', location='param')
parser.add_argument('Categories', type=str, help='movie category', location='param')
parser.add_argument('Tags', type=str, help='movie tags', location='param')


class TestMoviesMethods(unittest.TestCase):

    def test_Movies_Get(self):

        m = MoviesModel().get({})
        self.assertGreaterEqual(m.count(), MOVIE_LENGTH)

    def test_Movies_Get_ById(self):
        m = MoviesModel().getById(SAMPLE_OBJECT_ID)
        self.assertGreaterEqual(len(m.keys()), NUM_KEYS)

    def test_Movies_Get_By_Name(self):
        m = MoviesModel().get(SAMPLE_MOVIE_OBJECT)
        self.assertEqual(m.count(), MOVIE_LENGTH)
        