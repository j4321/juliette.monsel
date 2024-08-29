# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Juliette Monsel'
copyright = '2020-2024, Juliette Monsel'
author = 'Juliette Monsel'
html_title = 'My research webpage'
languages = ['en']
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.bibtex',
    'sphinxcontrib.openstreetmap',
    "sphinx.ext.autosectionlabel"
]
bibtex_bibfiles = ['conf.bib', 'publications.bib']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
# ~ html_theme = 'basic'

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
    ]
}

html_theme_options = {
    'fixed_sidebar': True,
    'show_powered_by': False,
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']

# intl
locale_dirs = ['locale/']   # path is example but recommended.
gettext_compact = False     # optional.

# --- compile CV
import os
path = os.getcwd()
import sys
sys.path.append(path)
from compile_CV import compile_CV
compile_CV()

# --- bibtex
from biblio_processing import MyStyle
from pybtex.plugin import register_plugin
register_plugin('pybtex.style.formatting', 'mystyle', MyStyle)

from rst_from_bib import generate_conf, generate_publi, generate_news
# generate publication and conference lists from bibtex files and generate news from news.json

generate_conf()
generate_publi()
generate_news()

# --- wordcloud picture
from generate_wordcloud import generate_wordcloud
generate_wordcloud()
