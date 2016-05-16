#! /usr/bin/env python

from __future__ import print_function

from json import load, dumps
from io import open

author_list = load(open("authors.json"))

with open("authors.json", "w", encoding='utf-8') as f:
    data = dumps(author_list, ensure_ascii=False, sort_keys=True, indent=4,
            separators=(',', ': '))
    f.write(data)
