FROM golang:1.25-alpine AS builder

WORKDIR /build

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o /life-logger ./cmd/app/main.go


FROM alpine:latest

RUN apk --no-cache add ca-certificates tzdata

WORKDIR /app
COPY --from=builder /life-logger .

RUN chmod +x /app/life-logger
CMD ["./life-logger"]
