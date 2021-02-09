#!/bin/bash

# Quick dev test, and it's OK to run it multiple times.
set -ex

virtualenv venv
source venv/bin/activate

pip install -U nose

nosetests -v tests/
