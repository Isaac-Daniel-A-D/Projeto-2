FROM alpine:latest

RUN apk add --no-cache curl

WORKDIR /monitor
COPY loop.sh .
RUN chmod +x loop.sh

CMD ["./loop.sh"]