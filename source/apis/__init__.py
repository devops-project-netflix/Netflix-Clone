from flask_restx import Api
from .movies import api as ns1

api = Api(
	version='1.0', 
	title='Netflix Clone APIs',
    description='The following APIs are used for Netflix clone',
)

api.add_namespace(ns1)
