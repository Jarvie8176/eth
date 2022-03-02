#!/usr/bin/env bash

pytest --mypy && coverage run -m pytest && coverage report -m
