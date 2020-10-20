#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:09:12 2020 by juliette
"""
import bibtexparser

# books
with open('books.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

if bib_database.entries:
    books = """
Books
-----
.. container:: publi

    .. bibliography:: books.bib
        :list: bullet
        :all:
        :style: mystyle
"""
else:
    books = ""

# preprints
with open('preprints.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

if bib_database.entries:
    preprints = """
Preprints
---------
.. container:: publi

    .. bibliography:: preprints.bib
        :list: bullet
        :all:
        :style: mystyle
    
Articles
--------
"""
else:
    preprints = """
Articles
--------
"""

# published articles
with open('publications.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)

years = set()
for entry in bib_database.entries:
    year = entry.get('year', '')
    if year:
        years.add(int(year))

years = sorted(years, reverse=True)
publi = """
.. rubric:: {year}

.. container:: publi

    .. bibliography:: publications.bib
        :list: bullet
        :filter: (not cited) and (year == "{year}")
        :style: mystyle
"""

with open("publications-list.rst", 'w') as file:
    file.write(books)
    file.write(preprints)
    file.write('\n'.join([publi.format(year=year) for year in years]))
