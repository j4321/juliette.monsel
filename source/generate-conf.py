#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:09:12 2020 by juliette
"""
import bibtexparser

with open('conf.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

dates = {'poster': set(), 
         'invited': set(),
         'contributed': set()}
         
for entry in bib_database.entries:
    year = entry.get('year', '')
    kind = entry.get('keywords', '')
    dates[kind].add(year) 

headers = {
    'invited': """
Invited talks and seminars
---------------------------
""",
    'contributed': """
Contributed talks
-----------------
""",
    'poster': """
Poster
------
"""
}

publi = """
.. rubric:: {year}

.. container:: publi

    .. bibliography:: conf.bib
        :list: bullet
        :filter: (not cited) and (year == "{year}") and (keywords == "{kind}")
        :style: mystyle
"""
with open("conf-list.rst", 'w') as file:
    for kind in ['invited', 'contributed', 'poster']:
        years = sorted(dates[kind], reverse=True)
        file.write(headers[kind])
        file.write('\n'.join([publi.format(year=year, kind=kind) for year in years]))

# ~ with open("publications-list.rst", 'w') as file:
    # ~ file.write(books)
    # ~ file.write(preprints)
    # ~ file.write('\n'.join([publi.format(year=year) for year in years]))
