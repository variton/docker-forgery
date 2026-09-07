#!/bin/sh
set -eu

# Generate and persist the lockfile for a newly created project.
if [ ! -f package-lock.json ]; then
  echo "package-lock.json not found; running npm install..."
  npm install
elif [ ! -d node_modules ]; then
  echo "node_modules not found; installing locked dependencies..."
  npm ci
fi

exec npm run dev -- --host 0.0.0.0
