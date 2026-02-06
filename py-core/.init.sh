#!/bin/bash
set -e
# set -x   # 👈 logs every command before it runs
export LAB=$PWD
export PATH=/root/.local/bin:$PATH
. /opt/py-core/.venv/bin/activate 
cd /opt/py-core
python3.12 updater.py
cd build
/root/.local/bin/uv sync --active
cd $LAB
exec /bin/bash -i
