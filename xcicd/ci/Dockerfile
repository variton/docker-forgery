FROM ubuntu:26.04

ENV INAME=xcicd
ENV DEBIAN_FRONTEND=noninteractive

USER root
WORKDIR /root

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      git \
      python3 \
      python3-pip \
      python3-venv \
      python3-pytest \
      python3-pytest-mock \
 && rm -rf /var/lib/apt/lists/*

COPY bashrc /root/.bashrc
COPY bash_aliases /root/.bash_aliases
COPY bash_env /root/.bash_env

WORKDIR /home/${INAME}
