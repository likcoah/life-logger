FROM alpine:latest

RUN apk --no-cache add ca-certificates tzdata

COPY ./bin/life-logger /app

RUN chmod +x /app

CMD ["/app"]
