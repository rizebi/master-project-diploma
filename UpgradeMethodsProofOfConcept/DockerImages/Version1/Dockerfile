from alpine:latest

RUN apk update

RUN apk add --no-cache python3 py-pip

WORKDIR /app

COPY FlaskRequirements.txt app.py /app/

RUN pip3 --no-cache-dir install -r FlaskRequirements.txt

ENTRYPOINT  ["python3"]

EXPOSE 7000

CMD ["app.py"]

