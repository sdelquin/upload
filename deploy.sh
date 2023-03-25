#!/bin/bash

cd "$(dirname "$0")"
git pull
source ~/.pyenv/versions/upload/bin/activate
pip install -r requirements.txt
supervisorctl restart upload
