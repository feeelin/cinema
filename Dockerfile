FROM python

#RUN apt-get update
#RUN apt-get install -y tdsodbc unixodbc-dev
#RUN apt install unixodbc-bin -y
#RUN apt-get clean -y
#
#RUN apt-get install libodbc2
#RUN apt-get install unixodbc-dev




RUN mkdir /web_django
WORKDIR /web_django
RUN python -m venv venv
RUN source venv/bin/activate

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./odbc.sh /web_django/
RUN ./odbc.sh

COPY ./requirements.txt /web_django/

RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /web_django/
