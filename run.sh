#!/bin/bash

source ~/.pyenv/versions/upload/bin/activate
cd "$(dirname "$0")"
exec flask --app main.py run --host=0.0.0.0
