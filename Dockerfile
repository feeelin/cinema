FROM python:3.11

ADD odbcinst.ini /etc/odbcinst.ini
RUN apt-get update
RUN apt-get install -y tdsodbc unixodbc-dev
RUN apt install unixodbc-bin -y
RUN apt-get clean -y

RUN apt install build-essential libgss3
RUN cd /tmp
RUN wget  https://download.microsoft.com/download/2/E/5/2E58F097-805C-4AB8-9FC6-71288AB4409D/msodbcsql-13.0.0.0.tar.gz
RUN tar xzvf msodbcsql-13.0.0.0.tar.gz
RUN cd msodbcsql-13.0.0.0
RUN ./build_dm.sh
RUN cd /tmp/unixODBC.24807.30156.17882/unixODBC-2.3.1; make install
RUN cd /tmp/msodbcsql-13.0.0.0
RUN ./install.sh install


RUN mkdir /web_django
WORKDIR /web_django

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /web_django/

RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/
