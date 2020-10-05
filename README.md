# Netflix-Clone

## Ammar bin Ayaz, Sujay Lokesh, Varun Ojha

Netflix Clone  
Create a video streaming web application that allows users to view video content from a library of video content (movies, TV shows).

Requirements:  
REST APIs for CRUD on video content  
Elasticsearch search on video content  
User specific content APIs. (To store videos currently being watched by user)  
Video stream functional module  
Login module (extra)  
Browsing history logging API

Implementations  
Create a basic microservice architecture design for the backend  
Incrementally create REST APIs on FLASK-RESTX  
Setup swagger for all the APIs  
Create a simple web interface using ReactJS. Web interface should be list all content for a user and then allow an user to stream a video content  
Tools to be used:  
Python Flask RestX  
ReactJS  
Elasticsearch  
MongoDB  
Docker  
Github

REST API:  
GET /home?user_id=1 (fetch list of movies)  
GET, POST, PUT, DELETE /videos  
GET, POST, PUT, DELETE /categories (movies, tv series, documentaries, news, comedy, kids, cartoon, anime)  
GET, POST, PUT, DELETE /tags (mystery, drama, horror)  
GET, POST, PUT, DELETE /user  
GET, PUT /user/{user_id}/preference  
/signin, signup, /verify

Microservice:  
USER - [auth, preference][barely scaled]  
CONTENT - [categories, tags, reference to videos][barely scaled][search]  
VIDEO Streaming [scaled demand] [Storage(S3, Cloud Storage)]

JSON stub

{
“Title”:”xyz”,
“Description”:”Information about the movie”,
“Categories”:[],
“Tags”:[]
“Storage”:[],
"Cast": []
}

Milestones  
Swagger functioning endpoints w tests  
Integrated with storage  
Streaming [w UI]  
User Accounts

Paradigm: dev, master, v,a,s branch

# Running the app on your local machine

Clone the Repository  
cd into requirements directory  
run pip install -r requirements.txt  
cd into source directory  
run ./local.sh

# Running the make file

Added makefile  
 To push code into github run `make prod`  
 To make a development environment run `make dev_env`  
 To run test cases run `make test`
