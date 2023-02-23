#!/usr/bin/env bash

clear

if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed." >&2
    exit 1
fi

echo "Installing every dependency..."
python3 -m pip install pypresence
clear
python3 index.py
