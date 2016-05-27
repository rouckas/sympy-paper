#! /usr/bin/env python

from __future__ import print_function

from io import open
from json import load

author_list = load(open("authors.json"))
author_list = list(filter(lambda x: x["sympy_commits"] > 0, author_list))

print("Generating authors_table.md")

with open("authors_table.md", "w", encoding='utf-8') as f:
    f.write(u"""\
# Article Authors

""")
    f.write(u"\n")
    f.write(u"| Author | Email | Institution | Institution Address |\n")
    f.write(u"| :---   | :---  | :---        | :---                |\n")

    for author in author_list:
        # Some authors used an alternate email address, not associated with
        # their GitHub profile, which causes GitHub not to show their commits
        # if we use the `github_id` field. For these authors we must use the
        # `sympy_commit_email` field.
        if "sympy_commit_email" in author:
            sympy_commit_id = author["sympy_commit_email"]
        else:
            sympy_commit_id = author["github_id"]
        f.write(u"| %s | %s | %s | %s |\n" % ( author["name"],
            author["email"], author["institution"],
            author["institution_address"], ))

    f.write(u"\n")
    f.write(u"Note: This file was automatically generated from "
        "`authors.json` using `authors_table.py`.\n")
