ARG UV_VERSION=0.13.1
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv

FROM ubuntu:26.04

ENV INAME=xphide

# Enable only when compiling dependencies or editing inside the container.
ARG INSTALL_DEV_TOOLS=false
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl openssl \
    && if [ "$INSTALL_DEV_TOOLS" = "true" ]; then \
        apt-get install -y --no-install-recommends build-essential vim; \
    fi \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY --from=uv /uv /uvx /usr/local/bin/
COPY bashrc /root/.bashrc
COPY bash_aliases /root/.bash_aliases
COPY bash_env /root/.bash_env

WORKDIR /home/${INAME}
CMD ["/bin/bash"]
