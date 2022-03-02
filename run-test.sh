#!/usr/bin/env bash

source .venv/bin/activate
pytest --mypy && coverage run -m pytest && coverage report -m
