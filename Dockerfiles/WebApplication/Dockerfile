from alpine:latest

RUN apk update

RUN apk add --no-cache python3-dev gcc libffi-dev musl-dev zlib-dev jpeg-dev curl openssl-dev py-pip

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app

RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip --no-cache-dir install -r requirements.txt

ENTRYPOINT  ["python3"]

CMD ["app.py"]