# Build the docker image
docker build -t ipycore:1.0 .

# Instance the container (has been prepared)
docker run --name=pycore --hostname=cypher -v $PWD:/home/pycore --net=host --restart=no -it ipycore:1.0 /bin/bash
