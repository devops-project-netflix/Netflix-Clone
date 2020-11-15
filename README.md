# Netflix-Clone

[![Coverage Status](https://coveralls.io/repos/github/devops-project-netflix/Netflix-Clone/badge.svg?branch=master2)](https://coveralls.io/github/devops-project-netflix/Netflix-Clone?branch=master2)

[![Actions Status](https://github.com/devops-project-netflix/Netflix-Clone/workflows/CI/badge.svg)](https://github.com/devops-project-netflix/Netflix-Clone/actions)

http://ec2-52-3-255-1.compute-1.amazonaws.com/

# Frontend  
For frontend please refer to below repo  
https://github.com/devops-project-netflix/Movie-Frontend  
# Completed Tasks

**Flask-RESTX API server setup**

**APIs for Movies, Categories, Tags**

**Make file for running tests and builds**

**Testcases using unittest**

**Integration of Frontend with the Backend**

**Hosting our application on AWS EC2**

**Building a CI/CD pipeline using Github actions**

**Create a docker executable**

Docker Command reference

docker build -t image_name .

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
"Cast": [],
"vote_average":rating as a number,
"vote_count":count of votes,
"id": identifier,
"status": Released or not,
"poster_path":path of poster in tmdb,
"homepage": link to the web,
"budget": Budget in dollars,
"backdrop_path": Url to its image,
"tagline":tagline for the movie
}

Milestones  
Swagger functioning endpoints w tests  
Integrated with storage  
Streaming [w UI]  
User Accounts

Paradigm: dev, master, v,a,s branch

# Running the app on your local machine

Clone the Repository  
`cd into requirements directory`  
run `pip install -r requirements.txt`  
`cd into source directory`  
run `./local.sh`

# Running the make file

Added makefile  
 To push code into github `run make prod`  
 To make a development environment run `make dev_env`

# Running the frontend

The Frontend is independent,The play functionality is not working for now  
and we are working on that.

# To run locally visit the frontend repo
The Frontend code is being maintained in a separate repo  
The cleanup of frontend will happen soon  
The Frontend is independent, and deployed on AWS amplify
Locally:  
Clone the Repo
 `npm install`  
 `npm start`  
 Demo Application running on AWS Amplify server  
 https://master.d3g8trqb4bccnl.amplifyapp.com/    
# Integration

The Integration of the frontend is complete with the backend  
Now just start the frontend and it will work  
It is referring to the deployed flask app on ec2

# CI/CD Pipeline

We are using GitHub Actions to handle our automated Testing.

On successful completion of the tests, we are connecting to AWS EC2 to pull a new version of the code.

Deployment scripts can be found under source/scripts/

CI/CD Workflow files can be found under .github/workflows
