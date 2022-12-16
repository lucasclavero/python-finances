FROM python:3.9 as base
WORKDIR /app
COPY . /app
RUN python /app/invoice-generator/setup.py install