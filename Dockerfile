FROM python:3.7
USER root

RUN apt-get update
RUN apt-get install -y vim less tree git
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN curl https://raw.githubusercontent.com/skxeve/dotfiles/master/install.sh | bash