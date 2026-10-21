# Build the docker image
docker build -t ghcr.io/variton/ixphide:1.0 .

# Optional: include compilers and Vim (increases image size)
docker build --build-arg INSTALL_DEV_TOOLS=true -t ghcr.io/variton/ixphide:dev .

# Instance the container (has been prepared)
docker run --name=xphide --hostname=morpheus -v $PWD:/home/xphide --net=host --restart=no -it ghcr.io/variton/ixphide:1.0 /bin/bash

The default image keeps Ubuntu, Bash, curl, OpenSSL, CA certificates, and uv/uvx.
It omits build-essential, Vim, and software-properties-common. Enable development
tools when Python dependencies need native compilation. Python itself is still
installed on demand by uv; no application or dependencies are bundled here.

Package installation and cleanup share one layer, recommended packages are
disabled, and uv binaries are copied from the official image (version controlled
by the UV_VERSION build argument). The build context includes only the Dockerfile
and shell configuration files.
