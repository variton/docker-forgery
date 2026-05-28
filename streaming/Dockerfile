FROM ubuntu:resolute

ENV INAME="cxx-core"

USER root
WORKDIR /root

RUN apt update
RUN apt upgrade -y
RUN apt install -y openssl  
RUN apt install -y curl 
RUN apt install -y build-essential
RUN apt install -y vim 
RUN apt install -y doxygen
RUN apt install -y graphviz
RUN apt install -y valgrind 
RUN apt install -y heaptrack
RUN apt install -y ninja-build
RUN apt install -y cmake
RUN apt install -y libspdlog-dev
RUN apt install -y libcurl4-openssl-dev
RUN apt install -y libfmt-dev
RUN apt install -y linux-tools-common 
RUN apt install -y linux-tools-generic
RUN apt install -y libexpected-dev 
RUN apt install -y python3-pip

# dependencies for gstreamer
RUN apt install -y gstreamer1.0-tools
RUN apt install -y gstreamer1.0-plugins-good
RUN apt install -y gstreamer1.0-plugins-bad 
RUN apt install -y gstreamer1.0-plugins-ugly

ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

WORKDIR /home/${INAME}
