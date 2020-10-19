import unittest
from flask_restx import Namespace
from models.categories import CategoriesModel, SAMPLE_OBJECT_CAT
from models.tags import TagsModel, HTML_OK, MOVIE_LENGTH, MOVIE_NOTFOUND,MOVIE


api = Namespace('Categories', description='all movies endpoints')
parser = api.parser()
parser.add_argument('name', type=str, help='category name', location='param')


class TestCategoriesMethods(unittest.TestCase):

    def test_Categories_Get(self):

        m = CategoriesModel().get({})
        self.assertGreaterEqual(m.count(), MOVIE_LENGTH)

    def test_Categories_Get_ById(self):
        m = CategoriesModel().getById(SAMPLE_OBJECT_CAT)
        self.assertEqual(m['name'], MOVIE)
