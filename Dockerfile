FROM jfloff/alpine-python:3.4-onbuild
COPY . /app
WORKDIR /app
ENV SERVER_HOST="0.0.0.0"
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["runserver.py"]