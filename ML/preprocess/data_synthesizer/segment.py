"""
These functions create list of list of segments (prefixes | bases | suffixes)
to be used as building blocks for synthetic words.
returns segments: segments grouped by syllable count, 
                should be list[list[string]]
                where segments[i] is a list of segments of i syllable count
"""

import os
import json


def prefix_words():
    MAX_PREFIX_SYLLABLE_COUNT = 8
    prefixes = [[] for _ in range(MAX_PREFIX_SYLLABLE_COUNT)]
    with open(f"{os.getcwd()}/data/prefixes_list.txt") as file:
        for line in file.readlines():
            word, syllable_count = line.strip().split("-")
            prefixes[int(syllable_count)].append(word)
    return prefixes


def dict_words():
    MAX_BASE_SYLLABLE_COUNT = 14
    base_words = [[] for _ in range(MAX_BASE_SYLLABLE_COUNT + 1)]
    with open(f"{os.getcwd()}/data/syllableCountDict.json") as file:
        for line in json.load(file).items():
            word, syllable_count = line
            base_words[int(syllable_count)].append(word)
    return base_words


def suffix_words():
    MAX_SUFFIX_SYLLABLE_COUNT = 6
    suffixes = [[] for _ in range(MAX_SUFFIX_SYLLABLE_COUNT)]
    with open(f"{os.getcwd()}/data/suffixes_list.txt") as file:
        for line in file.readlines():
            syllable_count, word = line.strip().split("-")
            suffixes[int(syllable_count)].append(word)
    return suffixes
