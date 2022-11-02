#!/bin/env python3

import sys
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
    exit("Screen name is required")

name = sys.argv[1]

with open("template.html") as template:
    contents = template.read()
    soup = BeautifulSoup(contents, "html.parser")
    soup.title.string = name.capitalize() + " - Adoolting"

    with open("screens/%s.html" % (name), "w") as target:
        target.write(soup.prettify())