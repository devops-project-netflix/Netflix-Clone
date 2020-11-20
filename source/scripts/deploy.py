import subprocess

p = subprocess.Popen(
    [
        "ssh",
        "-o",
        "StrictHostKeyChecking=no",
        "-i",
        "devops.pem",
        "ubuntu@ec2-52-72-32-138.compute-1.amazonaws.com",
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    universal_newlines=True,
    bufsize=0,
)

p.stdin.write("source /home/ubuntu/mypy36venv/bin/activate\n")
p.stdin.write("cd Netflix-Clone\n")
p.stdin.write("git reset --hard HEAD\n")
p.stdin.write("git pull\n")
p.stdin.write("cd source/scripts\n")
p.stdin.write("bash final_deployment.sh\n")
p.stdin.close()
print(p.stdout.read())
print("Done")
