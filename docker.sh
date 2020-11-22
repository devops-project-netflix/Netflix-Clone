#!/bin/bash

docker build -t netflix-clone-img .
docker run -it -p 80:5000 netflix-clone-img