# Build the docker image
docker build -t istreamer:1.0 .

# Instance the container (has been prepared)
docker run --name=streamer --hostname=cypher -v $PWD:/home/cxx-core --net=host --device=/dev/video0 --group-add video --restart=no -it istreamer:1.0 /bin/bash

## Remarks
This image is the root foundation to start a video stream.
It is not a development environment.
