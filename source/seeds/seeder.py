import os
import sys
from seeds.movies_seeder import *
from seeds.categories_seeder import *
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def database_seed():
    print("Running seeders ..")
    MoviesSeed().seed()
    CategoriesSeed().seed()
