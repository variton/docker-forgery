FROM golang:latest AS builder

RUN go install github.com/rhysd/actionlint/cmd/actionlint@latest

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
 && rm -rf /var/lib/apt/lists/*

# actionlint
COPY --from=builder /go/bin/actionlint /usr/local/bin/actionlint

# act
RUN curl -fsSL https://raw.githubusercontent.com/nektos/act/master/install.sh | bash \
 && mv ./bin/act /usr/local/bin/act \
 && rm -rf ./bin

# uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
 && mv /root/.local/bin/uv /usr/local/bin/uv \
 && mv /root/.local/bin/uvx /usr/local/bin/uvx

COPY bashrc /root/.bashrc
COPY bash_aliases /root/.bash_aliases
COPY bash_env /root/.bash_env

WORKDIR /home/${INAME}

# Verify tooling
RUN python3 --version \
 && pip3 --version \
 && pytest --version \
 && uv --version \
 && actionlint --version \
 && act --version
