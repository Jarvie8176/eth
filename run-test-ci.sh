#!/usr/bin/env bash

source .venv/bin/activate
bash run-test.sh && coverage xml
