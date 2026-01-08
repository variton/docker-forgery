# Build the docker image
docker build -t ipy-core:1.0 .

# Instance the container (has been prepared)
docker run --name=py-core --user "$(id -u):$(id -g)" --hostname=cypher -v $PWD:/home/py-core --net=host --restart=no -it ipy-core:1.0 /bin/bash
