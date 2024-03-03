#!/bin/bash

# checks if Python is installed on the system or not
python3 --version

# check if venv exists
if [ -d ".venv" ]; then
    echo ".venv - virtual environment present"
else
    python3 -m venv .venv
    echo ".venv - virtual environment created"
fi


#python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py