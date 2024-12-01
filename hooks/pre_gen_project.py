#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""pre_gen_project.py

Pre-generate project hook to take care of the download of the input of the puzzle.

*Package:* aoc_cookiecutter  
*Author:* Leon Geers
*Date:* Dec 2024  
"""

from pathlib import Path
import requests


def get_input(year: str | int, day: str | int, cookie: str) -> str:
    """Download the input for the given year and day.

    The cookie is the session cookie from AoC.
    """
    day_no = int(day) if isinstance(day, str) else day
    req = requests.get(f"https://adventofcode.com/{year}/day/{day_no}/input", headers={"cookie": f"session={cookie}"})
    req.raise_for_status()
    return req.text


YEAR = "{{ cookiecutter.year }}"
DAY = "{{ cookiecutter.day_number }}"
COOKIE = "{{ cookiecutter.session_cookie }}"

if __name__ == '__main__':
    filepath = Path("input")
    filepath.write_text(get_input(YEAR, DAY, COOKIE))
