#!/bin/bash

source ~/.pyenv/versions/upload/bin/activate
cd "$(dirname "$0")"
exec gunicorn -b unix:/tmp/upload.sock main:app
