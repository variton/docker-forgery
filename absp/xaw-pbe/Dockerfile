From ubuntu:26.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3.14 \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.12.19 /uv /usr/local/bin/

WORKDIR /xaw-pbe

COPY pyproject.toml uv.lock ./

RUN uv sync --locked

ENV PATH="/xaw-pbe/.venv/bin:$PATH"
ENV PYTHONPATH="/xaw-pbe/src"

COPY src/ ./src/
COPY tests/ ./tests/
COPY nr-tests/ ./nr-tests/

EXPOSE 7777

CMD ["uvicorn", "xawpbe:app", "--app-dir", "src", "--host", "0.0.0.0", "--port", "7777"]
