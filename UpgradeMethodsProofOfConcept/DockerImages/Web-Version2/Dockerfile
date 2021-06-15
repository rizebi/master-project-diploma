from alpine:latest

RUN apk update

RUN apk add --no-cache python3-dev gcc libffi-dev musl-dev zlib-dev jpeg-dev curl openssl-dev py-pip

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN CRYPTOGRAPHY_DONT_BUILD_RUST=1 pip --no-cache-dir install -r requirements.txt

COPY ./ /app

CMD ["/usr/bin/python3", "/app/app.py"]