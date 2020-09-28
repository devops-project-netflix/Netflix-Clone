import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from seeds.movies_seeder import *

def database_seed():
	#print("In seeder")
	MoviesSeed().seed()