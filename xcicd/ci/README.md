# Build the docker image
docker build -t ghcr.io/variton/ixcicd:1.0 .

# Instance the container
docker run --name=xcicd --hostname=cypher -v $PWD:/home/xcicd --net=host --restart=no -it ghcr.io/variton/ixcicd:1.0 /bin/bash
