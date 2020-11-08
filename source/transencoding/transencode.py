import ffmpeg_streaming
from ffmpeg_streaming import Formats, Bitrate, Representation, Size
from ffmpeg_streaming import S3, CloudManager
import os

import boto3
import sys
sys.setrecursionlimit(5000)

session = boto3.Session()
credentials = session.get_credentials()


print(credentials)


S3_KEY                    = credentials.access_key
S3_SECRET                 = credentials.secret_key
S3_REGION                 = session.region_name


s3 = S3(aws_access_key_id=S3_KEY, aws_secret_access_key=S3_SECRET, region_name=S3_REGION)

video = ffmpeg_streaming.input(s3, bucket_name="all-the-lambdas", key="sample-mp4-file.mp4")


# print("here")
save_to_s3 = CloudManager().add(s3, bucket_name="all-the-lambdas")
_360p  = Representation(Size(640, 360), Bitrate(276 * 1024, 128 * 1024))
_480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
_720p  = Representation(Size(1280, 720), Bitrate(2048 * 1024, 320 * 1024))

hls = video.hls(Formats.h264())
hls.representations(_360p, _480p, _720p)
hls.output(clouds=save_to_s3)
