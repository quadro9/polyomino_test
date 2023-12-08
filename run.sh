#!/bin/bash

sudo apt update
sudo apt install -y python3-pip python3-venv
python3 -m pip install -U pip

if [ ! -d ".venv" ] ; then
    python3 -m venv .venv
fi

source .venv/bin/activate
python3 -m pip install pytest

export COMMAND_RUN="./main.py"

python3 -m pytest --verbose --junitxml=tests/polynomio_tests.xml tests/
