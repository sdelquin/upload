#!/bin/bash

git pull
source ~/.pyenv/versions/upload/bin/activate
pip install -r requirements.txt
#supervisorctl restart gobcas
