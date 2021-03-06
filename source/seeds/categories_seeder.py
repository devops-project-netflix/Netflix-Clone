import os
import sys
from models.categories import CategoriesModel
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class CategoriesSeed:
    def __init__(self):
        cwd = os.getcwd()
        self.seed_file = cwd + '/seeds/data/categories.json'

    def seed(self):
        print("Categories seed ..")
        with open(self.seed_file) as json_file:
            data = json.load(json_file)
            for index in range(len(data)):
                category = CategoriesModel().get({'name': data[index]['name']})
                category = [doc for doc in category]
                if(0 == len(category)):
                    CategoriesModel().insert(data[index])
