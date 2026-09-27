# Build the docker image
docker build -t ghcr.io/variton/ixaw-pbe:1.0 .

# Instance the container (has been prepared)
docker run --name=xaw-pbe --hostname=cypher -v $PWD:/home/xaw-pbe --net=host --restart=no -it ghcr.io/variton/ixaw-pbe:1.0 /bin/bash
