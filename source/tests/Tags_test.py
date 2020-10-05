import unittest

from flask import Flask, request
from flask_restx import Resource, Api, fields, marshal_with, reqparse, Namespace
import json
from db import *
from bson import json_util
from models.movies import MoviesModel
from models.tags import TagsModel
from utilities.responses import *
import itertools

import json

from apis.tags import Movies

api = Namespace('Tags', description='all movies tag endpoints')

parser = api.parser()
parser.add_argument('id', type=list, help='ID', location='param')



class TestTagsMethods(unittest.TestCase):

    def test_Movies_Get(self):
        m = Movies().get()
        self.assertEqual(m.status,"200 OK")

    def test_MoviebyTag_Found_Get(self):
        objectTag = "Drama"
        movies = TagsModel().getByTag({objectTag})
        self.assertGreaterEqual(len(movies),1)

    def test_MoviebyTag_NotFound_Get(self):
        objectTag = "NotFound"
        movies = TagsModel().getByTag({objectTag})
        self.assertEqual(len(movies),0)
    
    def test_MovieRecommendations_Get(self):
        watched = ['5f716d74cffb4d9a4a5f8704','5f716d74cffb4d9a4a5f8707']
        movies = TagsModel().getRecommendations(watched)
        self.assertEqual(m.status,"200 OK")

