#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate the word cloud image for index.html using the python libraries:
    - Pillow (PIL)
    - NumPy
    - WordCloud https://doi.org/10.5281/zenodo.7901644
    - ArXiv Update CLI https://gitlab.com/j_4321/arxivscript

Created on Mon May 29 12:08:12 2023 by Juliette Monsel
"""
from wordcloud import WordCloud, STOPWORDS
from arxiv_update_cli import api_general_query
from PIL import Image
import numpy as np
import re
from socket import error as SocketError

re_latex = re.compile(r"\$.*?\$")


def color_func(word, font_size, position, orientation, font_path, random_state):
    x = random_state.uniform(0, 1)
    r, g, b = np.array((x, 0.25, 1 - x))*255
    return ("#%2.2x%2.2x%2.2x%2.2x" % (int(r), int(g), int(b), 255)).upper()


def generate_wordcloud(**kw):
    # retrieve articles
    author = "Juliette Monsel"
    abstracts = []
    try:
        for article in api_general_query(f'au:%22{"+".join(author.split())}%22'):
            txt = " ".join(article['summary'].splitlines())
            abstracts.append(txt)
    except SocketError as e:
        print(f"\033[31mUnable to fetch data to generate worldcloud image: {e}.\033[0m")
        return
    if len(abstracts) == 0:
        print("No papers found")
        return
    abstracts = re_latex.sub("", "\n\n".join(abstracts)).lower()
    # generate wordcloud
    stopwords = set(STOPWORDS)
    more_stopwords = {'We', 'paper', 'new', 'article', 'show', 'evidence', "shown",
                      'demonstrate', 'highlight', "with", "within", "first", "second",
                      "parameter", "number", "visible", "achieve", "achieved",
                      "showed", "evidenced", "and", "or", "emphasize", "study",
                      "compared", "play", "constant", "result", "different", "provide", "find"}
    stopwords = stopwords.union(more_stopwords)

    mask = np.array(Image.open("assets/wc_mask2.png"))

    wc_kw = dict(
        background_color="#ffffff00",
        stopwords=stopwords,
        max_words=200,
        max_font_size=100,
        min_font_size=6,
        random_state=42,
        # color_func=lambda *x, **k: "red",
        color_func=color_func,
        mask=mask,
        min_word_length=4,
        mode="RGBA",
        font_path="/usr/share/fonts/liberation/LiberationMono-Regular.ttf"
    )
    wc_kw.update(kw)
    wordcloud = WordCloud(**wc_kw)
    wordcloud.generate(abstracts)
    with open("assets/wordcloud.svg", "w") as file:
        file.write(wordcloud.to_svg())
