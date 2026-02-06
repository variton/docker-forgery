# Build the docker image
docker build -t ghcr.io/variton/ipy-core:1.0 .

# Instance the container (has been prepared) if an entrypoint has not been defined
docker run --name=py-core --hostname=cypher -v $PWD:/home/py-core --net=host --restart=no -it ghcr.io/variton/ipy-core:1.0 /bin/bash

# Instance the container (has been prepared) if an entrypoint has been defined
docker run --name=py-core --hostname=cypher -v $PWD:/home/py-core --net=host --restart=no -it ghcr.io/variton/ipy-core:1.0
