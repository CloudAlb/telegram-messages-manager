FROM alpine:3.20.2

RUN apk update && apk upgrade --no-cache

RUN apk add --no-cache python3=3.12.3-r1 && \
  apk add pipx=1.6.0-r0

# Set environment variables
ENV USER_NAME=builder
ENV USER_UID=1001
ENV USER_GID=1001

RUN addgroup -g $USER_GID $USER_NAME && \
    adduser -D -u $USER_UID -G $USER_NAME $USER_NAME

WORKDIR /home/$USER_NAME/myapp
ENTRYPOINT ["./runDev.sh"]
