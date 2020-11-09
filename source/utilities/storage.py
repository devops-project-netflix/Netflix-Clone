import logging
import boto3
from botocore.exceptions import ClientError

from config import VIDEO_CONTENT_BUCKET


s3 = boto3.client("s3")

# s3 = boto3.client(
#    "s3",
#    aws_access_key_id=S3_KEY,
#    aws_secret_access_key=S3_SECRET
# )

def upload(file):
    s3_upload_file(file, VIDEO_CONTENT_BUCKET)

def s3_upload_file(file, bucket_name, acl="public-read"):

    try:

        s3.upload_fileobj(
            file,
            bucket_name,
            file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e