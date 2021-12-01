#!/usr/bin/env bash
bash /app/wait.sh "$host:5432" -- bash /app/init.sh
python main.py
