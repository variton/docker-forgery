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
 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /go/bin/actionlint /usr/local/bin/actionlint

RUN curl -fsSL https://raw.githubusercontent.com/nektos/act/master/install.sh | bash \
 && mv ./bin/act /usr/local/bin/act \
 && rm -rf ./bin /tmp/*

COPY bashrc /root/.bashrc
COPY bash_aliases /root/.bash_aliases
COPY bash_env /root/.bash_env

WORKDIR /home/${INAME}
