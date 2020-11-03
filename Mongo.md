# INTRODUCTION  

Mongo DB is an open source document database built on a horizontal scale out architecture. Instead of storing data in tabular format like SQL databases, each row in Mongo DB is a document described in JSON. It is a great option if you don’t know the structure of the data when you are starting to design your application. This kind of unstructured approach allows variations in the structure of the data. It also provides functionalities required for querying the data or indexing the data to enhance the search performance.  

# Choice of Implementation of Mongo DB  

For our project we decided to use the cloud version of Mongo DB i.e MongoDB Atlas. It provides a multi cloud architecture for the data base which is ideal for Agile development. It provides option to choose Cloud service provider, we are using AWS  
as our provider. To make the connection from our system it provides a connection string which we passed in the mongo client. We are using Pymongo distribution to interact with Mongo DB.  

# Why Mongo DB ?

1> Centralised storage of data : When we are working in a team, if we keep a local storage of the data then we will run into issues of synchronisation. To avoid any such issue it is better if we make a central data repository so that every team member is in sync.  

2> Flexibility: This is a point which really stands out. If we are doing incremental development we don't have the exact model when we start the development process. The structure of the data changes with time and having a NoSQL DB really helps in this regard. Just to cite a real example a week back we were integrating our backend with the frontend and for frontend we needed some extra keys in the data. And we were able to do this seamlessly and effortlessly as we were using Mongo DB as our database.  

3> Cloud access: Using a cloud provider really makes our life much easier where we don't have to worry about having the same data points and go through the process of installation of the software on our local machine. I would like to share an experience. One day I was away from my system and we were facing some issue because of data which needed some changes in the DB. I logged in using my phone and made the required changes, talk about ease of access.  

4> Mongo DB provides flexibility to develops as it can be used with multiple programming languages. And it also provides many methods to query and search data from the DB. Querying the DB is very simple and easy to use. For us it took no more than 1 day to get started and learn the basics enough to implement it in our project.



# Setting up mongo db atlas for the project  
1) Create a mongo db atlas account  
2) Create the project in your organisation  
3) Create the cluster where you will store your data. 
   Follow https://docs.atlas.mongodb.com/tutorial/create-new-cluster/  
4) Once the cluster is made, get the connection string  
5) We are using pymongo library to interact with mongo db  
6) We have created a separate file to make the connection. 
   There we just have to write the below code to make the connection  
 # CONNECTION_STRING = "connection_string_from_atlas"    
 # client = pymongo.MongoClient(CONNECTION_STRING)  
 # db = client.get_database(database)

