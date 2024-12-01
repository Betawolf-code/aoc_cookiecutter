#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""post_gen_project.py

Post-generate project hook for substituting the story into the day 1, assignment 1 file and the testdata.

*Package:* aoc_cookiecutter  
*Author:* Leon Geers
*Date:* Dec 2024
"""

import textwrap
from pathlib import Path

import requests
from bs4 import element, BeautifulSoup


def get_page(year: str | int, day: str | int, cookie: str) -> str:
    """Download the page with puzzle explanation from AoC for the given year and day.

    The cookie is the session cookie from AoC.
    """
    day_no = int(day) if isinstance(day, str) else day
    req = requests.get(f"https://adventofcode.com/{year}/day/{day_no}", headers={"cookie": f"session={cookie}"})
    req.raise_for_status()
    return req.text


def extract_story(html_source: str) -> element.Tag:
    """Extract the story from the html page."""
    soup = BeautifulSoup(html_source, 'html.parser')
    res = soup.article
    return res


def parse_html(elem: element.Tag) -> str:
    """Parse the html in the element in human readable form to go in the module description."""
    text = ""
    for e in elem.descendants:
        match e:
            case str():
                text += e.strip() + " "
            case a if a.name in ("br", "p", "h1", "h2", "h3", "h4", "tr", "th", "pre"):
                text += "\n\n" if a.name == "p" else "\n"
            case a if a.name == "li":
                text += "\n- "
    splitlines = ["\n".join(textwrap.wrap(line, width=120)) for line in text.splitlines()]
    return "\n".join(splitlines)


def get_examples(elem: element.Tag) -> list[str]:
    """Extract the examples from the element (which should be an article from AoC)."""
    res = []
    # Find all the preformatted tags
    for pre_tag in elem.find_all("pre"):
        # Check for each whether they're preceded by a paragraph with the word 'example' in there and containing a child
        # of type 'code'.
        if "example" not in pre_tag.find_previous_sibling().text or pre_tag.next.name != "code":
            continue
        res.append(pre_tag.text)
    return res


YEAR = "{{ cookiecutter.year }}"
DAY = "{{ cookiecutter.day_number }}"
COOKIE = "{{ cookiecutter.session_cookie }}"

if __name__ == '__main__':
    page = get_page(YEAR, DAY, COOKIE)
    story = extract_story(page)
    story_text = parse_html(story)

    # Now fill in the story in the day's first assignment code file
    day_file = Path("{{ cookiecutter.__day_name }}_1.py")
    code_text = day_file.read_text()
    code_text = code_text.replace("**STORY**", story_text)
    day_file.write_text(code_text)

    # And put the examples in the testdata variable of inputdata
    inputdata_file = Path("{{ cookiecutter.__day_name }}/inputdata.py")
    inputdata_text = inputdata_file.read_text()
    examples = get_examples(story)
    inputdata_text = inputdata_text.replace("testdata = None", f"testdata = {examples}")
    inputdata_file.write_text(inputdata_text)
