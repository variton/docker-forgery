FROM ubuntu:24.04 

ENV INAME="py-core"

USER root
WORKDIR /root

RUN apt update
RUN apt upgrade -y
RUN apt install -y openssl curl build-essential
RUN apt install -y software-properties-common
RUN apt install -y python3-pip vim virtualenv

ADD local-ci.sh /home/${INAME}/local-ci.sh
ADD pre-shippping.sh /home/${INAME}/pre-shippping.sh
ADD pyproject.toml /home/${INAME}/pyproject.toml
ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

#download uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
#source all env
RUN . ~/.bashrc
#set up virtual env
RUN /root/.local/bin/uv venv .${INAME}

WORKDIR /home/${INAME}
