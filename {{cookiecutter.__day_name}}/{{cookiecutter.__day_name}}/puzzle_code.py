# -*- coding: utf-8 -*-
r"""puzzle_code.py

Puzzle code for Advent of Code {{cookiecutter.year}} day {{cookiecutter.day_number}} for both assignments

*Package:* Advent of Code {{cookiecutter.year}}
*Author:* {{ cookiecutter.full_name }}
*Date:* {{cookiecutter.__date}}
"""

from typing import Any
from {{cookiecutter.__day_name}}.inputdata import data, testdata

def preprocess_data(inputdata: str) -> Any:
    """Put your preprocessing routine here for the input data."""
    return inputdata.splitlines()

