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
RUN apt install -y valgrind 
RUN apt install -y heaptrack
RUN apt install -y ninja-build
RUN apt install -y cmake
RUN apt install -y linux-tools-common 
RUN apt install -y linux-tools-generic
RUN apt install -y python3-pip

# dependencies for ffmpeg and v4l2
RUN apt install -y v4l-utils 
RUN apt install -y ffmpeg

# dependencies for gstreamer
RUN apt install -y libgstreamer1.0-dev
RUN apt install -y gstreamer1.0-tools
RUN apt install -y gstreamer1.0-plugins-good
RUN apt install -y gstreamer1.0-plugins-bad 
RUN apt install -y gstreamer1.0-plugins-ugly

# dependencies for config
RUN apt install -y nlohmann-json3-dev

ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

WORKDIR /home/${INAME}
