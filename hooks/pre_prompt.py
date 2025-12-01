#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pre_prompt.py

Run the prescript hook to add the session cookie

*Package:* aoc_cookiecutter  
*Author:* Leon Geers
*Date:* Dec 2024  
"""

import os
from cookiecutter import generate
import json
import sys

if sys.platform == "linux":
    USER = os.environ.get("USER", "")
else:
    USER = os.environ.get("USERNAME", "")


if __name__ == '__main__':
    COOKIE = os.environ["AOC_SESSIONCOOKIE"]

    context = generate.generate_context()
    context["cookiecutter"].update({
        'session_cookie': COOKIE,
        'full_name': USER
    })
    with open('cookiecutter.json', 'w') as f:
        json.dump(context['cookiecutter'], f, indent=2)
