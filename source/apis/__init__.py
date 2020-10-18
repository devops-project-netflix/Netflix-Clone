from flask_restx import Api
from .movies import api as m
from .categories import api as c
from .tags import api as t

api = Api(
    version='1.0', 
    title='Netflix Clone APIs',
    description='The following APIs are used for Netflix clone',
)

api.add_namespace(m)
api.add_namespace(c)
api.add_namespace(t)
