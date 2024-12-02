# -*- coding: utf-8 -*-
r"""test_{{cookiecutter.__day_name}}.py

Tests for day {{cookiecutter.day_number}} of Advent of Code {{cookiecutter.year}}.

*Package:* Advent of Code {{cookiecutter.year}}
*Author:* {{ cookiecutter.full_name }}
*Date:* {{cookiecutter.__date}}
"""

from {{cookiecutter.__day_name}} import testdata, preprocess_data

def test_{{ cookiecutter.__day_name }}():
    preproc_data = preprocess_data(testdata[0])
    assert False
