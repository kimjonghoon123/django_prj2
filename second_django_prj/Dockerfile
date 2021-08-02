# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev #--(5.2)

COPY . /usr/src/app/
# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# FROM python:3.8
# ENV PYTHONUNBUFFERED=1
#
#
# WORKDIR /usr/src/app
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt


#FROM python:3.8.0-alpine
#RUN pip3 install --upgrade pip
##
##RUN apk add mysql-dev mysql-client gcc python3-dev musl-dev zlib-dev jpeg-dev
##RUN pip3 install cryptography
##set work directory 프로젝트 작업폴더를 /usr/src/app으로 지정한다.
#WORKDIR /usr/src/app
#
##set environment variable
#ENV PYTHONDONTWRITEBYTECODE 1
##파이썬은 종종 소스 코드를 컴파일해서 확장자가 .pyc인 파일을 생성한다. 도커를 이용할때는 pyc가 필요하지 않아 .pyc를 생성하지 않게 한다.
#ENV PYTHONUNBUFFERED 1
##파이썬 로그가 버퍼링없이 즉각적으로 출력하게 한다.
#RUN pip3 install --upgrade pip
#RUN apk update
#RUN apk add mysql-dev mysql-client gcc python3-dev musl-dev zlib-dev jpeg-dev
##mysql-dev mysql-client
##RUN apk add --no-cache \
##        libressl-dev \
##        musl-dev \
##        libffi-dev && \
##    pip3 install --upgrade pip --no-cache-dir cryptography==3.3.1 && \
##    apk del \
##        libressl-dev \
##        musl-dev \
##        libffi-dev
##requirements.txt에서 살펴본 라이브러리를 설치하기 위해 필요한 gcc, musl-dev등을 미리 설치한다.
##오류가 나서 2시간동안 미칠뻔햇다.  찾아보고 위에거를 더 추가하니 해결됐다.
#
#COPY . /usr/src/app/
##로컬 컴퓨터의 현재위치에 있는 모든 파일을 작업폴더로 복사한다.(/usr/src/app/으로)
##install dependencies
#
#RUN pip install -r requirements.txt
#requiredments.txt에 나열된 라이브러리를 설치한다.
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#WORKDIR /usr/src/app
#
#RUN apk add --no-cache  libressl-dev musl-dev libffi-dev && pip install --no-cache-dir cryptography==2.1.4 &&
#    apk del libressl-dev musl-dev libffi-dev
#RUN apk add mysql-dev mysql-client gcc python3-dev musl-dev zlib-dev jpeg-dev
#RUN apk update
#
#COPY . /usr/src/app/
#
#RUN pip install -r requirements.txt
#
#ENV DOCKERIZE_VERSION v0.6.1
#RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
#    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
#ENTRYPOINT ["dockerize", "-wait", "tcp://mysql_service:3306", "-timeout", "20s"]


#
#ENV MYSQL_USER newuser
#ENV MYSQL_PASSWORD 1234
#
## docker 컨테이너 내부 DB에 root계정 password 생성
#ENV MYSQL_ROOT_HOST %
#ENV MYSQL_ROOT_PASSWORD whdgns1002@
#
## docker 컨테이너 내부 DB에 database 이름 생성
#ENV MYSQL_DATABASE django
#COPY n3-testdb.sql /docker-entrypoint-initdb.d/
#set work directory 프로젝트 작업폴더를 /usr/src/app으로 지정한다.
WORKDIR /usr/src/app

#set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
#파이썬은 종종 소스 코드를 컴파일해서 확장자가 .pyc인 파일을 생성한다. 도커를 이용할때는 pyc가 필요하지 않아 .pyc를 생성하지 않게 한다.
ENV PYTHONUNBUFFERED 1
#파이썬 로그가 버퍼링없이 즉각적으로 출력하게 한다.

#RUN apk update
#RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev
#
#RUN apk add --no-cache \
#        libressl-dev \
#        musl-dev \
#        libffi-dev && \
#    pip install --upgrade pip --no-cache-dir cryptography==3.3.1 && \
#    apk del \
#        libressl-dev \
#        musl-dev \
#        libffi-dev
##requirements.txt에서 살펴본 라이브러리를 설치하기 위해 필요한 gcc, musl-dev등을 미리 설치한다.
##오류가 나서 2시간동안 미칠뻔햇다.  찾아보고 위에거를 더 추가하니 해결됐다.
#
#COPY . /usr/src/app/
##로컬 컴퓨터의 현재위치에 있는 모든 파일을 작업폴더로 복사한다.(/usr/src/app/으로)
##install dependencies
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
##requiredments.txt에 나열된 라이브러리를 설치한다.

