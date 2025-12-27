# Build the docker image
docker build -t ghcr.io/variton/ixpylib:1.0 .

# Instance the container (has been prepared)
docker run --name=xpylib --hostname=cypher -v $PWD:/home/xpylib --net=host --restart=no -it ghcr.io/variton/ixpylib:1.0 /bin/bash
