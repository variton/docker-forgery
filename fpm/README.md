# FPM Docker Image

This folder contains a small Docker image for running [`fpm`](https://fpm.readthedocs.io/), a packaging tool that builds packages such as `.deb`, `.rpm`, and tar archives from a simple command-line interface.

The image is based on `debian:bookworm-slim`. It installs `fpm` in a builder stage and copies only the installed Ruby gems into the final runtime image.

## Build

```sh
docker build -t local/fpm .
```

## Usage

Run `fpm` from the current directory by mounting it into the container:

```sh
docker run --rm -v "$PWD:/work" local/fpm --help
```

Example package build:

```sh
docker run --rm -v "$PWD:/work" local/fpm \
  -s dir \
  -t deb \
  -n example-package \
  -v 1.0.0 \
  ./package-root/=/
```

## Notes

- The container uses `/work` as its working directory.
- The entrypoint is `fpm`, so arguments passed to `docker run` are forwarded directly to `fpm`.
- Package build inputs and outputs should be placed in the mounted working directory.
