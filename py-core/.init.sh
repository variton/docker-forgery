#!/usr/bin/env sh
set -e
# set -x   # 👈 logs every command before it runs
. /opt/py-core/bin/activate 
cd /opt
/root/.local/bin/uv sync --active

exec /bin/bash -i
