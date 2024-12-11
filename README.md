# FARMING_SITE
displays crops in a farm and their prices. 
the webapp is not yet complete .
also has a dashboard where users can chat.

## Setup
1. clone the repo
2. build the docker container:
    docker build -t esthers_web:farming -f ./Dockerfile .
3. run the container:
    docker run -p 8000:8000 esthers_web:farming
5. access via browser at http://localhost:8000
