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

p.stdin.write("cd Netflix-Clone")
p.stdin.write("git reset --hard HEAD")
p.stdin.write("git pull")
p.stdin.write("cd source/scripts")
p.stdin.write("bash final_deployment.sh")
p.stdin.close()
count = 0
for line in iter(p.stdout.readline, b''):
    if count <= 50:
        print(">>> " + line.rstrip())
        count += 1
    else:
        break
print("Done")
