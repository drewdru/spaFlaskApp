#!/bin/bash
export FLASK_APP=./src/main.py
source ../env/bin/activate
flask run -h 0.0.0.0