FROM ubuntu:26.04 

ENV INAME="xcicd"

USER root
WORKDIR /root

RUN apt update
RUN apt upgrade -y

RUN apt install -y golang-go 
RUN apt install -y curl 

ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

# actionlint
RUN go install github.com/rhysd/actionlint/cmd/actionlint@latest
# act
RUN curl https://raw.githubusercontent.com/nektos/act/master/install.sh | bash

WORKDIR /home/${INAME}
