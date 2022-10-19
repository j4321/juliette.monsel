"""
Custom pybtex style to display my publication list and conferences
"""
import re
import json

from pybtex.style.formatting.alpha import Style as PlainStyle
from pybtex.style.sorting import BaseSortingStyle
import datetime
from pybtex.style.formatting import toplevel
from pybtex.style.template import (
    tag, field, optional, names, optional_field, sentence, words, first_of, join, href
)
from pybtex.style.names import BaseNameStyle, name_part
from pybtex.richtext import Symbol, Text
from pybtex.database import parse_file


class NameStyle(BaseNameStyle):

    def format(self, person, abbr=False):
        r"""
        Format names similarly to {ff~}{vv~}{ll}{, jj} in BibTeX.

        >>> from pybtex.database import Person
        >>> name = Person(string=r"Charles Louis Xavier Joseph de la Vall{\'e}e Poussin")
        >>> plain = NameStyle().format

        >>> print(plain(name).format().render_as('latex'))
        Charles Louis Xavier~Joseph de~la Vall{é}e~Poussin
        >>> print(plain(name).format().render_as('html'))
        Charles Louis Xavier&nbsp;Joseph de&nbsp;la Vall<span class="bibtex-protected">é</span>e&nbsp;Poussin

        >>> print(plain(name, abbr=True).format().render_as('latex'))
        C.~L. X.~J. de~la Vall{é}e~Poussin
        >>> print(plain(name, abbr=True).format().render_as('html'))
        C.&nbsp;L. X.&nbsp;J. de&nbsp;la Vall<span class="bibtex-protected">é</span>e&nbsp;Poussin

        >>> name = Person(first='First', last='Last', middle='Middle')
        >>> print(plain(name).format().render_as('latex'))
        First~Middle Last

        >>> print(plain(name, abbr=True).format().render_as('latex'))
        F.~M. Last

        >>> print(plain(Person('de Last, Jr., First Middle')).format().render_as('latex'))
        First~Middle de~Last, Jr.

        """
        name =  join[
            name_part(tie=True, abbr=abbr)[person.rich_first_names + person.rich_middle_names],
            name_part(tie=True)[person.rich_prelast_names],
            name_part[person.rich_last_names],
            name_part(before=', ')[person.rich_lineage_names]
        ]
        if str(person) == "Monsel, Juliette":
            return tag("em")[name]
        return name


class SortingStyle(BaseSortingStyle):

    def sorting_key(self, entry):
        year = entry.fields.get('year', '')
        if not year.isdigit():
            # preprint
            year =  f"20{entry.fields['eprint'][:2]}"
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
        self.name_style = NameStyle()
        self.format_name = self.name_style.format
        # ~ self.label_style = LabelStyle()
        # ~ self.format_labels = self.label_style.format_labels

    def get_conference_template(self, e):
        template = toplevel [
            sentence [
                self.format_title(e, 'title', as_sentence=False),
                optional[ self.format_editor(e, as_sentence=False) ],
                tag('strong') [field('booktitle')],
                # ~self.format_btitle(e, 'booktitle', as_sentence=False),
                self.format_volume_and_series(e, as_sentence=False),
                self.format_chapter_and_pages(e),
                optional_field('note'),
                optional_field('publisher'),
                optional_field('location'),
                self.format_edition(e),
                optional_field('dates'),
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
        url = self.format_link(e)
        journal = sentence [
             field('journal'),
             optional[ volume_and_pages ]
        ]
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
           href [ url, journal ],
            sentence [ optional_field('note') ],
            # self.format_web_refs(e),
        ]
        return template

    def get_book_template(self, e):
        template = toplevel [
            self.format_author_or_editor(e),
            href [self.format_link(e), self.format_btitle(e, 'title')],
            self.format_volume_and_series(e),
            sentence [
                field('publisher'),
                optional_field('location'),
                self.format_edition(e),
                field('year')
            ],
            optional[ sentence [ self.format_isbn(e) ] ],
            sentence [ optional_field('note') ],
            # self.format_web_refs(e),
            optional[ sentence [ self.format_phd(e) ] ],
        ]
        return template

    def format_url(self, e):
        # based on urlbst format.url
        return href [
            field('url', raw=True),
            field('url', raw=True)
        ]

    def format_link(self, e):
        return first_of [
            optional_field("url", raw=True),
            optional  [
                join [
                    'https://doi.org/',
                    field('doi', raw=True)
                ]
            ],
            optional [
                join [
                    'https://arxiv.org/abs/',
                    field('eprint', raw=True)
                ],
            ]
        ]

    def get_booklet_template(self, e):
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence [
                optional_field('howpublished'),
                optional_field('location'),
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
                optional_field('location'),
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
                optional_field('location'),
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
                self.format_location_organization_publisher_date(e),
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
                optional_field('location'),
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
                optional_field('location'),
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
                optional_field('location'),
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
                    self.format_location_organization_publisher_date(e),
                ],
            ]
        else:
            main_part = [
                optional [ sentence [ field('organization') ] ],
                sentence [
                    self.format_btitle(e, 'title', as_sentence=False),
                    self.format_volume_and_series(e, as_sentence=False),
                    self.format_location_organization_publisher_date(
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
                optional_field('location'),
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

    def format_names(self, role, as_sentence=True):
        formatted_names = names(role, sep=', ', sep2 = ' and ', last_sep=', and ')
        if as_sentence:
            return sentence [formatted_names]
        else:
            return formatted_names


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

    def format_phd(self, e):
        # based on urlbst format.url
        return words [
            'The initial version of my PhD dissertation is available ',
            href [
                field('phd', raw=True),
                'here'
                ]
        ]

    def format_btitle(self, e, which_field, as_sentence=True):
        formatted_title = field(which_field)
        if as_sentence:
            return sentence[ formatted_title ]
        else:
            return formatted_title

    def format_title(self, e, which_field, as_sentence=True):
        formatted_title = field(
            which_field, apply_func=lambda text: f'"{text.capitalize()}"'
        )
        if as_sentence:
            return sentence [ formatted_title ]
        else:
            return formatted_title


class NewsStyle(PlainStyle):
    def format_field(self, field, entry):
        context = {
            'entry': entry,
            'style': self,
            'bib_data': None,
        }
        get_template = getattr(self, 'get_{}_template'.format(field))
        return str(get_template(entry).format_data(context))

    def get_authors_template(self, e):
        formatted_names = names("author", sep=', ', sep2 = ' and ', last_sep=', ')
        return formatted_names

    def get_title_template(self, e):
        return self.format_title(e, "title", False)

    def get_date_template(self, e):
        return words [optional_field('month'), field('year')]

    def get_link_template(self, e):
        return first_of [
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ]
        ]

    def get_reference_template(self, e):
        if e.type == "misc":
            return join [
                'arXiv:',
                field('eprint', raw=True)
            ]
        else: # article
            volume_and_pages = first_of [
                # volume and pages, with optional issue number
                optional [
                    join [
                        field('volume'),
                        optional['(', field('number'), ')'],
                        ', ', pages
                    ],
                ],
                # pages only
                words ['pages', pages],
            ]
            return words [
                field('journal'),
                optional[ volume_and_pages ]
            ]

    def format_url(self, e):
        # based on urlbst format.url
        return field('url', raw=True),

    def format_pubmed(self, e):
        # based on urlbst format.pubmed
        return join [
            'https://www.ncbi.nlm.nih.gov/pubmed/',
            field('pubmed', raw=True)
        ]

    def format_doi(self, e):
        # based on urlbst format.doi
        return join [
            'https://doi.org/',
            field('doi', raw=True)
        ]

    def format_eprint(self, e):
        # based on urlbst format.eprint
        return join [
            'https://arxiv.org/abs/',
            field('eprint', raw=True)
        ]

def bibtex_to_json(key):
    """Print json data corresponding to entry KEY in piublications.bib"""
    bib_data = parse_file("publications.bib")
    style = NewsStyle()
    entry = bib_data.entries[key]
    data = entry.fields
    json_data = {}
    json_data["header"] = "New preprint" if entry.type == "misc" else "New article"
    json_data["date"] = style.format_field("date", entry)
    json_data["title"] = style.format_field("title", entry)
    json_data["authors"] = style.format_field("authors", entry)
    json_data["summary"] = data.get("abstract", "")
    json_data["links"] = [{"reference": style.format_field("reference", entry), "link": style.format_field("link", entry)}]
    json_data["note"] = data.get("note", "")
    return print(json.dumps({key: json_data}, indent=4))
