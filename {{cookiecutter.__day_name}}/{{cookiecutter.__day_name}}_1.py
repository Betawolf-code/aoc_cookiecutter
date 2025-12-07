# -*- coding: utf-8 -*-  # noqa: D400
"""{{ cookiecutter.__day_name}}_1.py

Advent of code {{cookiecutter.year}} - day {{cookiecutter.day_number}}
Assignment 1

**STORY**

*Package:* Advent of Code {{cookiecutter.year}}
*Author:* {{ cookiecutter.full_name }}
*Date:* {{cookiecutter.__date}}
"""

from {{cookiecutter.__day_name}} import (data, testdata, preprocess_data, part1)  # noqa


if __name__ == "__main__":
    preproc_data = preprocess_data(data)
    print(part1(preproc_data))
