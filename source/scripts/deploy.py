import subprocess



p = subprocess.Popen(['ssh','-o','StrictHostKeyChecking=no','-i','devops.pem','ubuntu@ec2-52-3-255-1.compute-1.amazonaws.com'],stdin=subprocess.PIPE, stdout=subprocess.PIPE,universal_newlines=True,bufsize=0)

p.stdin.write("source /home/ubuntu/myvenv/bin/activate \n")
p.stdin.write("bash final_deployment.sh")
p.stdin.close()
print("Done")