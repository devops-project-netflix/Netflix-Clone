# Netflix-Clone

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
“Description”:”blah”,
“Categories”:[],
“Tags”:[]
“Storage”:[]
}

Milestones
Swagger functioning endpoints w tests
Integrated with storage
Streaming [w UI]
User Accounts

Paradigm: dev, master, v,a,s branch

 

