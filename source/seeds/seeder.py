import os
import sys
from seeds.movies_seeder import MoviesSeed
from seeds.categories_seeder import CategoriesSeed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def database_seed():
    print("Running seeders ..")
    MoviesSeed().seed()
    CategoriesSeed().seed()
