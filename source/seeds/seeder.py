import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seeds.movies_seeder import *
from seeds.categories_seeder import *

def database_seed():
	print("Running seeders ..")
	MoviesSeed().seed()
	CategoriesSeed().seed()