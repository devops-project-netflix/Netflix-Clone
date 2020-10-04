from flask_pymongo import pymongo
def connect_to_database(database):
    CONNECTION_STRING = "mongodb+srv://ammar:abcd123@cluster0.8f754.mongodb.net/movies-db?retryWrites=true&w=majority"
    client = pymongo.MongoClient(CONNECTION_STRING)
    db = client.get_database(database)
<<<<<<< HEAD
    #print("Database context")
    #print(db)
=======
    print("Database context")
    print(db)
    print("\n\n")
>>>>>>> 5242da7c44fb9895deeb2bef76b56e1ae63f9f24
    return db
