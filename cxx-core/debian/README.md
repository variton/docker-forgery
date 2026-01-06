# Build the docker image
docker build -t igcc-14:1.0 .

# Instance the container (has been prepared)
docker run --name=cgcc-14 --hostname=cypher -v $PWD:/home/cxx-core --net=host --restart=no -it igcc-14:1.0 /bin/bash
