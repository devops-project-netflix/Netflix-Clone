import os

import boto3
import sys
sys.setrecursionlimit(5000)

session = boto3.Session()
credentials = session.get_credentials()


S3_KEY                    = "NEED TO REPLACE"
S3_SECRET                 = "NEED TO REPLACE WITH SECRETS"
S3_REGION                 = "us-west-1"

MONGO_CONNECTION_STRING = "mongodb+srv://ammar:abcd123@cluster0.8f754.mongodb.net/movies-db?retryWrites=true&w=majority"

VIDEO_CONTENT_BUCKET = "netflix-clone-bucket"