FROM debian:bookworm-slim AS fpm-builder

ENV GEM_HOME=/opt/gems
ENV PATH=/opt/gems/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ruby ruby-dev build-essential ca-certificates rubygems && \
    gem install --no-document fpm && \
    rm -rf /var/lib/apt/lists/*

FROM debian:bookworm-slim

ENV GEM_HOME=/opt/gems
ENV PATH=/opt/gems/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      ruby ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY --from=fpm-builder /opt/gems /opt/gems

WORKDIR /work

ENTRYPOINT ["fpm"]
