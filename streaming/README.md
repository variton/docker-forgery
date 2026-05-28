# Build the docker image
docker build -t istreamer:1.0 .

# Instance the container (has been prepared)
docker run --name=streamer --hostname=cypher -v $PWD:/home/cxx-core --net=host --restart=no -it istreamer:1.0 /bin/bash
