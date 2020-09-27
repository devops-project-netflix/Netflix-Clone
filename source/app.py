from flask import Flask, request
from flask_restx import Resource, Api, fields, marshal_with, reqparse
import json
from db import *
from bson import json_util
from seeds.seeder import database_seed
from apis import api

app = Flask(__name__)
api.init_app(app)
database_seed()

if __name__ == '__main__':
    app.run(debug=True)

# 1. Standardize the REST in movies
# 2. Add the categories REST 
# 3. Check for better swagger
# 4. Environment file for flask
# 5. Standard requests and response