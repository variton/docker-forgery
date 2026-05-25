# Build the docker image
docker build -t ghcr.io/variton/islimci:1.0 .

# Instance the container (has been prepared) if an entrypoint has not been defined
docker run --name=slimci --hostname=cypher -v $PWD:/home/py-ci --net=host --restart=no -it ghcr.io/variton/islimci:1.0 /bin/bash

# Instance the container (has been prepared) if an entrypoint has been defined
docker run --name=slimci --hostname=cypher -v $PWD:/home/py-ci --net=host --restart=no -it ghcr.io/variton/islimci:1.0
