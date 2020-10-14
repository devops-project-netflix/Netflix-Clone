import unittest

from flask import Flask, request
from flask_restx import Resource, Api, fields, marshal_with, reqparse, Namespace
import json
from db import *
from bson import json_util
#from models.movies import MoviesModel
from models.movies import MoviesModel, NUM_KEYS, SAMPLE_OBJECT_ID
from utilities.responses import *
import itertools

import json

from apis.movies import Movies

api = Namespace('Movies', description='all movies endpoints')

parser = api.parser()
parser.add_argument('Title', type=str, help='movie name', location='param')
parser.add_argument('Categories', type=str, help='movie category', location='param')
parser.add_argument('Tags', type=str, help='movie tags', location='param')


class TestMoviesMethods(unittest.TestCase):

    def test_Movies_Get(self):

        m = MoviesModel().get({})
        self.assertGreaterEqual(m.count(), 1)


    def test_Movies_Get_ById(self):
        m = MoviesModel().getById(SAMPLE_OBJECT_ID)
        #print (m.keys())
        self.assertGreaterEqual(len(m.keys()), NUM_KEYS)



