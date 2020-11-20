import unittest

from flask_restx import Namespace
from models.movies import MoviesModel, NUM_KEYS
from models.movies import SAMPLE_OBJECT_ID, SAMPLE_MOVIE_OBJECT
from models.movies import MOVIE_OBJECT
from models.tags import MOVIE_LENGTH

api = Namespace("Movies", description="all movies endpoints")

parser = api.parser()
parser.add_argument("Title", type=str, help="movie name", location="param")
parser.add_argument("Categories", type=str, help="category", location="param")
parser.add_argument("Tags", type=str, help="movie tags", location="param")


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

    def test_Movies_Post(self):
        inserted = MoviesModel().insert(MOVIE_OBJECT)
        fetch_inserted = MoviesModel().getById(inserted.inserted_id)
        self.assertEqual(MOVIE_OBJECT["Title"], fetch_inserted["Title"])
        inserted_id = inserted.inserted_id
        inserted = MoviesModel().delete(inserted_id)

    def test_Movies_Delete(self):
        inserted = MoviesModel().insert(MOVIE_OBJECT)
        inserted_id = inserted.inserted_id
        inserted = MoviesModel().delete(inserted_id)
        deleted = MoviesModel().getById(inserted_id)
        self.assertIsNone(deleted)
