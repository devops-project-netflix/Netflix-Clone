declare AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY AWS_SESSION_TOKEN
get_aws_creds_local () {
   # Use this to get secrets on a non AWS host assuming you've set credentials via some mechanism in the past, and then don't pass in a profile to gitlab-runner because it doesn't see the ~/.aws/credentials file where it would look up profiles
   awsProfile=${AWS_PROFILE:-default}
   AWS_ACCESS_KEY_ID=$(aws --profile $awsProfile configure get aws_access_key_id)
   AWS_SECRET_ACCESS_KEY=$(aws --profile $awsProfile configure get aws_secret_access_key)   
}

get_aws_creds_local

fuser -k 80/tcp
sudo docker stop $(sudo docker ps -aq)
sudo docker rm $(sudo docker ps -aq)
sudo docker rmi $(sudo docker images -q)
sudo docker pull devopsnetflix/devops:latest

sudo docker run -d -p 80:5000 --env AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --env AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY devopsnetflix/devops:latest
