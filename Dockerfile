#Deriving the latest base image
FROM python:latest

ADD ./validtest.py /

RUN pip install cffi
RUN pip install html-testRunner


CMD [ "python", "./validtest.py"]