import unittest

from flask import Flask, request
from flask_restx import Resource, Api, fields, marshal_with, reqparse, Namespace
import json
from db import *
from bson import json_util
#from models.movies import MoviesModel
from models.categories import CategoriesModel
from utilities.responses import *
import itertools

import json

from apis.movies import Movies

api = Namespace('Categories', description='all movies endpoints')

parser = api.parser()
parser.add_argument('name', type=str, help='category name', location='param')


class TestCategoriesMethods(unittest.TestCase):

    def test_Categories_Get(self):

        m = CategoriesModel().get({})
        self.assertGreaterEqual(m.count(), 1)


    def test_Categories_Get_ById(self):
        id = '5f716d75cffb4d9a4a5f8708'
        m = CategoriesModel().getById(id)
        #print (m.keys())
        self.assertEqual(m['name'], 'Movie')



