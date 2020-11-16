import os

import boto3
import sys
sys.setrecursionlimit(5000)

session = boto3.Session()
credentials = session.get_credentials()


S3_KEY                    = "AKIAVD7Q7SPR4CS764YV"
S3_SECRET                 = "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"
S3_REGION                 = "us-west-1"

MONGO_CONNECTION_STRING = "mongodb+srv://ammar:abcd123@cluster0.8f754.mongodb.net/movies-db?retryWrites=true&w=majority"

VIDEO_CONTENT_BUCKET = "netflix-clone-bucket"