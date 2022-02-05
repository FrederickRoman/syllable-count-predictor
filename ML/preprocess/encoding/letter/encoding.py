import numpy as np
import json

ALL_LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NB_LETTERS = len(ALL_LETTERS)
DIMS = NB_LETTERS + 1
MAX_WORD_LEN = 36
NUM_OF_WORDS = 657084


def encode_char(char):
    if char in ALL_LETTERS:
        return one_hot_encode(ALL_LETTERS.index(char), NB_LETTERS)
    else:
        return one_hot_encode(NB_LETTERS, NB_LETTERS)


def encode_word(word):
    encoded_word = np.array([encode_char(char) for char in word])
    num_empty_chars = MAX_WORD_LEN - len(word)
    empty_char_encoding = np.zeros((1, DIMS), dtype=int)
    for _ in range(num_empty_chars):
        encoded_word = np.append(encoded_word, empty_char_encoding, axis=0)
    return encoded_word


def one_hot_encode(num, max):
    encoding = np.zeros(shape=(max + 1), dtype=int)
    encoding[num] = 1
    return encoding


def encode():
    with open("../../../../data/syllableCountDict.json") as f:
        syllable_count_dict = json.load(f)
    xs = np.zeros(shape=(NUM_OF_WORDS, MAX_WORD_LEN, 27), dtype=int)
    ys = np.zeros(shape=(NUM_OF_WORDS, 1), dtype=int)
    for i, item in enumerate(syllable_count_dict.items()):
        word, syllable_count = item
        xs[i][:][:] = np.array([encode_word(word)])
        ys[i][:][:] = syllable_count
    return xs, ys
