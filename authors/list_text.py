#! /usr/bin/env python

from __future__ import print_function

from io import open
from json import load

author_list = load(open("authors.json"))
author_list = list(filter(lambda x: x["sympy_commits"] > 0, author_list))

print("Generating authors.md")

with open("authors.md", "w", encoding='utf-8') as f:
    f.write(u"""\
# Article Authors

All authors satisfy the following ICMJE [criteria](http://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html#two) for authorship:

1. Substantial contributions to the conception or design of the work; or the
   acquisition, analysis, or interpretation of data for the work; AND

2. Drafting the work or revising it critically for important intellectual
   content; AND

3. Final approval of the version to be published; AND

4. Agreement to be accountable for all aspects of the work in ensuring that
   questions related to the accuracy or integrity of any part of the work are
   appropriately investigated and resolved.


The column `SymPy Commits` lists how many commits the authors contributed to
SymPy (with a link to the actual commits), which shows how the requirement 1.
is satisfied.

The column `Article Contributions` lists all commits and comments to the
article itself, which shows how the requirement 2. is satisfied.

All authors approved the final version of the article, satisfying the
requirement 3.

Finally, all authors agreed to the requirement 4.

""")
    f.write(u"\n")
    f.write(u"| Author | GitHub Profile | SymPy Commits | "
            "Article Contributions | Affiliation |\n")
    f.write(u"| :---   | :---           |     :---:     | "
            ":---                  | :---        |\n")

    for author in author_list:
        # Some authors used an alternate email address, not associated with
        # their GitHub profile, which causes GitHub not to show their commits
        # if we use the `github_id` field. For these authors we must use the
        # `sympy_commit_email` field.
        if "sympy_commit_email" in author:
            sympy_commit_id = author["sympy_commit_email"]
        else:
            sympy_commit_id = author["github_id"]
        f.write(u"| %s | [@%s](https://github.com/%s) | "
            "[%d](https://github.com/sympy/sympy/commits?author=%s) | "
            "[commits](https://github.com/sympy/sympy-paper/commits?author=%s),"
                " [comments](https://github.com/sympy/sympy-paper/search"
                "?q=commenter:%s&type=Issues) "
            "| %s, %s |\n" % (
                author["name"],
                author["github_id"], author["github_id"],
                author["sympy_commits"], sympy_commit_id,
                author["github_id"], author["github_id"],
                author["institution"], author["institution_address_siam"],
                ))

    f.write(u"\n")
    f.write(u"Note: This file was automatically generated from "
        "`authors.json` using `list_text.py`.\n")
