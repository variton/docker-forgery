# Build the docker image
docker build -t icxx-resolute:1.0 .

# Instance the container (has been prepared)
docker run --name=cxx-resolute --hostname=cypher -v $PWD:/home/cxx-core --net=host --restart=no -it icxx-resolute:1.0 /bin/bash
