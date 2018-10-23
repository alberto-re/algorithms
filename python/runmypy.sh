#!/usr/bin/env bash

python -m mypy \
  test algo/sorting \
  algo/shuffling \
  algo/expression_evaluation \
  --ignore-missing-imports
