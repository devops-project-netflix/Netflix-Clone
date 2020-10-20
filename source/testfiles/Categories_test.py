import unittest,time
from flask_restx import Namespace
from models.categories import CategoriesModel, SAMPLE_OBJECT_CAT, TEST_OBJECT
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

    def test_Categories_Post(self):
    	inserted = CategoriesModel().insert(TEST_OBJECT)
    	fetch_inserted = CategoriesModel().getById(inserted.inserted_id)
    	self.assertEqual(TEST_OBJECT['name'],fetch_inserted['name'])

    def test_Categories_Delete(self):
    	inserted = CategoriesModel().insert(TEST_OBJECT)
    	inserted_id = inserted.inserted_id
    	inserted = CategoriesModel().delete(inserted_id)
    	deleted = CategoriesModel().getById(inserted_id)
    	self.assertIsNone(deleted)