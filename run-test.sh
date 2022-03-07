#!/usr/bin/env bash

source .venv/bin/activate
bash run-load-test-fixture.sh
pytest --mypy && coverage run -m pytest && coverage report -m
