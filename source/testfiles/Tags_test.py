import unittest
from flask_restx import Namespace
from models.tags import TagsModel, SAMPLE_OBJECT_ARRAY, TAGS_ARRAY, HTML_OK, MOVIE_LENGTH, MOVIE_NOTFOUND
from apis.tags import Movies

api = Namespace('Tags', description='all movies tag endpoints')

parser = api.parser()
parser.add_argument('id', type=list, help='ID', location='param')


class TestTagsMethods(unittest.TestCase):

    def test_Movies_Get(self):
        m = Movies().get()
        self.assertEqual(m.status, HTML_OK)

    def test_MoviebyTag_Found_Get(self):
        movies = TagsModel().getByTag({TAGS_ARRAY[0]})
        self.assertGreaterEqual(len(movies), MOVIE_LENGTH)

    def test_MoviebyTag_NotFound_Get(self):
        movies = TagsModel().getByTag({TAGS_ARRAY[1]})
        self.assertEqual(len(movies), MOVIE_NOTFOUND)

    def test_MovieRecommendations_Get(self):
        movies = TagsModel().getRecommendations(SAMPLE_OBJECT_ARRAY)
        self.assertGreaterEqual(len(movies), MOVIE_NOTFOUND)
