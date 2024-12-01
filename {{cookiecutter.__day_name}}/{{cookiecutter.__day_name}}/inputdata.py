# -*- coding: utf-8 -*-  # noqa: D400
"""inputdata.py

Input data

*Package:* Advent of Code {{cookiecutter.year}}
*Author:* {{ cookiecutter.full_name }}
*Date:* {{cookiecutter.__date}}
"""

from pathlib import Path

path = Path(__file__).parents[1]

if not (path / "input").exists():
    raise FileNotFoundError("Input not found")
else:
    with open(path / "input", "r") as f:
        data = f.read()

testdata = None
