FROM alpine:3.15

RUN apk add --no-cache python3 py3-pip && \
    pip install docker

COPY app/ /app

CMD ["python3", "-u", "/app/main.py"]
