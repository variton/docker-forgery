FROM debian:trixie

ENV INAME="cxx-core"

USER root
WORKDIR /root

RUN apt update
RUN apt upgrade -y
RUN apt install -y openssl  
RUN apt install -y curl 
RUN apt install -y build-essential
RUN apt install -y python3-pip pipx
RUN apt install -y vim 
RUN apt install -y python3.13-venv 
RUN apt install -y doxygen
RUN apt install -y graphviz
RUN apt install -y gcc-14
RUN apt install -y valgrind 
RUN apt install -y heaptrack
RUN apt install -y ninja-build
RUN apt install -y cmake
# RUN create another container that contain the following tools
# RUN apt install -y linux-tools-common 
# RUN apt install -y linux-tools-$(uname -r)
# RUN apt install -y rr

ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

#set up conan
RUN pipx ensurepath
#source all env
RUN . ~/.bashrc
#set up virtual env
RUN python3.13 -m venv $HOME/.$INAME
#activate venv
RUN . /root/.${INAME}/bin/activate
#install conan
RUN pipx install conan

WORKDIR /home/${INAME}
