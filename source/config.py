import os

import boto3
import sys
sys.setrecursionlimit(5000)

session = boto3.Session()
credentials = session.get_credentials()


S3_KEY                    = os.environ.get('AWS_ACCESS_KEY_ID')
S3_SECRET                 = os.environ.get('AWS_SECRET_ACCESS_KEY')
S3_REGION                 = "us-west-1"

MONGO_CONNECTION_STRING = "mongodb+srv://ammar:abcd123@cluster0.8f754.mongodb.net/movies-db?retryWrites=true&w=majority"

VIDEO_CONTENT_BUCKET = "netflix-clone-bucket"