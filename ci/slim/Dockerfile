FROM python:3.14-slim 

ENV INAME="py-ci"

USER root
WORKDIR /root

ADD bashrc /root/.bashrc
ADD bash_aliases /root/.bash_aliases
ADD bash_env /root/.bash_env

#source all env
RUN . ~/.bashrc
WORKDIR /home/${INAME}
#ENTRYPOINT ["/root/.local/.init.sh"]
