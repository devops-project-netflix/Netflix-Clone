from flask_pymongo import pymongo
def connect_to_database(database):
    CONNECTION_STRING = "mongodb+srv://ammar:abcd123@cluster0.8f754.mongodb.net/movies-db?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.get_database(database)
    #print("Database context")
    #print(db)
    return db
