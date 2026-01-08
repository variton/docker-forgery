#!/usr/bin/env sh
set -e
# set -x   # 👈 logs every command before it runs

. /root/.py-core/bin/activate
cd /home/$INAME
/root/.local/bin/uv sync --active

exec /bin/bash -i
