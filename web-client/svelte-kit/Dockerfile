
FROM node:26.8.1-alpine

WORKDIR /app

COPY bootstrap.sh /usr/local/bin/sveltekit-bootstrap
RUN chmod +x /usr/local/bin/sveltekit-bootstrap

EXPOSE 5173

ENTRYPOINT ["sveltekit-bootstrap"]
