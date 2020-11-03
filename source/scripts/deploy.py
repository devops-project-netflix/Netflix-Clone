import subprocess

import boto3

s3_client = boto3.client('s3')
s3_client.download_file('devopsnyu','devops.pem', 'devops.pem')


p = subprocess.Popen(['ssh','-i','devops.pem','ubuntu@ec2-52-3-255-1.compute-1.amazonaws.com'],stdin=subprocess.PIPE, stdout=subprocess.PIPE,universal_newlines=True,bufsize=0)

p.stdin.write("sudo fuser -k 80/tcp\n")

p.stdin.write("cd Netflix-Clone\n")

p.stdin.write("git pull\n")
p.stdin.write("cd source\n")
p.stdin.write("source /home/ubuntu/myvenv/bin/activate \n")



p.stdin.write("psudo ./local.sh\n")
p.stdin.write("logout\n")
p.stdin.close()
print("Done")