# Build the docker image
docker build -t isvelte:1.0 .

# Instance the container (has been prepared)
docker run --name=svelte --hostname=cypher -v $PWD:/home/xaw-fe --net=host -it isvelte:1.0 /bin/bash

## Remarks
This image is the root foundation to develope with the svelte kit.
