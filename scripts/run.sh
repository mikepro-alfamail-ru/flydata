#!/usr/bin/env bash

set -euxo pipefail

/app/wait.sh "$host:5432" -- /app/init.sh
python main.py
