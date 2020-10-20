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
copyright = '2020, Juliette Monsel'
author = 'Juliette Monsel'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxcontrib.bibtex'
]

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



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']

# --- bibtex
from pybtex.style.formatting.alpha import Style as PlainStyle
# ~ from pybtex.style.labels import BaseLabelStyle
from pybtex.style.sorting import BaseSortingStyle
import datetime
from pybtex.style.formatting import toplevel
from pybtex.style.template import (
    tag, field, optional, optional_field, sentence, words, first_of, join, href
)
from pybtex.richtext import Symbol, Text
# ~ from collections import Counter
from pybtex.plugin import register_plugin
import re

#~class LabelStyle(BaseLabelStyle):
#~    def format_labels(self, sorted_entries):
#~        labels = [self.format_label(entry) for entry in sorted_entries]
#~        count = Counter(labels)
#~        counted = Counter()
#~        for label in labels:
#~            if count[label] == 1:
#~                yield label
#~            else:
#~                yield label + chr(ord('a') + counted[label])
#~                counted.update([label])

#~    def format_labels(self, sorted_entries):
#~        labels = [self.format_label(entry) for entry in sorted_entries]
#~        for label in labels:
#~            yield label

#~    def format_label(self, entry):
#~        if "year" in entry.fields:
#~            return entry.fields["year"]
#~        else:
#~            return "??"
#~        # bst additionally sets sort.label

class SortingStyle(BaseSortingStyle):

    def sorting_key(self, entry):
        year = entry.fields.get('year', '')
        month = entry.fields.get('month', '')
        if month and year:
            date = datetime.datetime.strptime('{} {}'.format(month, year), '%b %Y')
        elif year:
            date = datetime.datetime(year=int(year), month=1, day=1)
        else:
            date = datetime.datetime.now()
        return date

    def sort(self, entries):
        entry_dict = dict(
            (self.sorting_key(entry), entry)
            for entry in entries
        )
        sorted_keys = sorted(entry_dict, reverse=True)
        sorted_entries = [entry_dict[key] for key in sorted_keys]
        return sorted_entries


def dashify(text):
    dash_re = re.compile(r'-+')
    return Text(Symbol('ndash')).join(text.split(dash_re))


pages = field('pages', apply_func=dashify)


class MyStyle(PlainStyle):
    default_label_style = 'alpha'

    def __init__(self, *args, **kwargs):
        super(MyStyle, self).__init__(*args, **kwargs)
        self.sorting_style = SortingStyle()
        self.sort = self.sorting_style.sort
        # ~ self.label_style = LabelStyle()
        # ~ self.format_labels = self.label_style.format_labels

    def get_conference_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            sentence [
                optional[ self.format_editor(e, as_sentence=False) ],
                self.format_btitle(e, 'booktitle', as_sentence=False),
                self.format_volume_and_series(e, as_sentence=False),
                self.format_chapter_and_pages(e),
            ],
            sentence [
                optional_field('publisher'),
                optional_field('address'),
                self.format_edition(e),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_article_template(self, e):
        volume_and_pages = first_of [
            # volume and pages, with optional issue number
            optional [
                join [
                    field('volume'),
                    optional['(', field('number'), ')'],
                    ':', pages
                ],
            ],
            # pages only
            words ['pages', pages],
        ]
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence [
                tag('em') [field('journal')],
                optional[ volume_and_pages ]
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    #~def get_book_template(self, e):
    #~    template = toplevel [
    #~        self.format_author_or_editor(e),
    #~        self.format_btitle(e, 'title'),
    #~        self.format_volume_and_series(e),
    #~        sentence [
    #~            field('publisher'),
    #~            optional_field('address'),
    #~            self.format_edition(e),
    #~        ],
    #~        optional[ sentence [ self.format_isbn(e) ] ],
    #~        sentence [ optional_field('note') ],
    #~        self.format_web_refs(e),
    #~    ]
    #~    return template

    def get_booklet_template(self, e):
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence [
                optional_field('howpublished'),
                optional_field('address'),
                optional_field('note'),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_inbook_template(self, e):
        template = toplevel [
            self.format_author_or_editor(e),
            sentence [
                self.format_btitle(e, 'title', as_sentence=False),
                self.format_chapter_and_pages(e),
            ],
            self.format_volume_and_series(e),
            sentence [
                field('publisher'),
                optional_field('address'),
                optional [
                    words [field('edition'), 'edition']
                ],
                optional_field('note'),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_incollection_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            words [
                'In',
                sentence [
                    optional[ self.format_editor(e, as_sentence=False) ],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_chapter_and_pages(e),
                ],
            ],
            sentence [
                optional_field('publisher'),
                optional_field('address'),
                self.format_edition(e),
            ],
            self.format_web_refs(e),
        ]
        return template

    def get_inproceedings_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            words [
                'In',
                sentence [
                    optional[ self.format_editor(e, as_sentence=False) ],
                    self.format_btitle(e, 'booktitle', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    optional[ pages ],
                ],
                self.format_address_organization_publisher_date(e),
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_manual_template(self, e):
        # TODO this only corresponds to the bst style if author is non-empty
        # for empty author we should put the organization first
        template = toplevel [
            optional [ sentence [ self.format_names('author') ] ],
            self.format_btitle(e, 'title'),
            sentence [
                optional_field('organization'),
                optional_field('address'),
                self.format_edition(e),
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_mastersthesis_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            sentence[
                "Master's thesis",
                field('school'),
                optional_field('address'),
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_misc_template(self, e):
        template = toplevel [
            optional[ sentence [self.format_names('author')] ],
            optional[ self.format_title(e, 'title') ],
            sentence[
                optional[ field('howpublished') ],
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_phdthesis_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_btitle(e, 'title'),
            sentence[
                'PhD thesis',
                field('school'),
                optional_field('address'),
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_proceedings_template(self, e):
        if 'editor' in e.persons:
            main_part = [
                self.format_editor(e),
                sentence [
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_address_organization_publisher_date(e),
                ],
            ]
        else:
            main_part = [
                optional [ sentence [ field('organization') ] ],
                sentence [
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_address_organization_publisher_date(
                        e, include_organization=False),
                ],
            ]
        template = toplevel [
            main_part + [
                sentence [ optional_field('note') ],
                self.format_web_refs(e),
            ]
        ]
        return template

    def get_techreport_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            sentence [
                words[
                    first_of [
                        optional_field('type'),
                        'Technical Report',
                    ],
                    optional_field('number'),
                ],
                field('institution'),
                optional_field('address'),
            ],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template

    def get_unpublished_template(self, e):
        template = toplevel [
            sentence [self.format_names('author')],
            self.format_title(e, 'title'),
            sentence [
                field('note'),
            ],
            self.format_web_refs(e),
        ]
        return template

    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence [
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            optional [ self.format_video(e) ],
        ]

    def format_video(self, e):
        # based on urlbst format.url
        return words [
            'Video:',
            href [
                field('video', raw=True),
                field('video', raw=True)
                ]
        ]


register_plugin('pybtex.style.formatting', 'mystyle', MyStyle)
