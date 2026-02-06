FROM ubuntu:24.04 

ENV INAME="py-core"

USER root
WORKDIR /root

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y build-essential 
RUN apt-get install -y software-properties-common 
RUN apt-get install -y openssl 
RUN apt-get install -y curl 
RUN apt-get install -y python3-pip 
RUN apt-get install -y vim 
RUN apt-get install -y virtualenv 
RUN apt-get install -y pipx
RUN pipx ensurepath

ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

#download uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
#source all env
RUN . ~/.bashrc
#install conf handler
RUN pipx install remarshal
RUN mkdir -p /opt/${INAME}
ADD pyproject.toml /opt/${INAME}
ADD updater.py /opt/${INAME}
#create venv
WORKDIR /opt/${INAME}
RUN /root/.local/bin/uv venv
ADD local-ci.sh /root/.local/.local-ci
ADD .init.sh /root/.local/.init.sh
ADD pre-shippping.sh /root/.local/.pre-shippping
WORKDIR /home/${INAME}
ENTRYPOINT ["/root/.local/.init.sh"]
