#Deriving the latest base image
FROM python:latest

ADD ./validtest.py /
RUN mkdir rapport_template
ADD ./rapport_template/index.html /rapport_template

RUN pip install cffi
RUN pip install html-testRunner


CMD [ "python", "./validtest.py"]