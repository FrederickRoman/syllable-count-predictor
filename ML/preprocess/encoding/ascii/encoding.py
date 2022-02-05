import json
import numpy as np

NUM_OF_WORDS = 657084
MAX_WORD_LEN = 33 # 125
DIMS = 5
NB_CLASSES = 15


def encode_char(char):
    if char.isalpha():
        binaryArray = [int(bit) for bit in bin(ord(char) - 97).replace("0b", "")]
        binaryArrayLen = len(binaryArray)
        if binaryArrayLen < DIMS:
            zero_pad = np.zeros((DIMS - binaryArrayLen), dtype=int)
            return np.concatenate((zero_pad, binaryArray))
        else:
            return binaryArray
    else:
        return [1, 1, 1, 1, 1]


def encode_word(word):
    encoded_word = np.array([encode_char(char) for char in word])  # .flatten()
    num_empty_chars = MAX_WORD_LEN - len(word)
    empty_char_encoding = np.zeros((1, DIMS), dtype=int)
    for i in range(num_empty_chars):
        encoded_word = np.append(encoded_word, empty_char_encoding, axis=0)
    return encoded_word


def one_hot_encode(num, max):
    encoding = np.zeros(shape=(max + 1), dtype=int)
    encoding[num] = 1
    return encoding


def encode_syllable_count(syllable_count):
    return one_hot_encode(syllable_count, NB_CLASSES - 1)


def encode():
    with open("../../../../data/syllableCountDict.json") as f:
        syllable_count_dict = json.load(f)
    xs = np.zeros(shape=(NUM_OF_WORDS, MAX_WORD_LEN * DIMS), dtype=int)
    ys = np.zeros(shape=(NUM_OF_WORDS, NB_CLASSES), dtype=int)
    for i, item in enumerate(syllable_count_dict.items()):
        word, syllable_count = item
        encoded_word = encode_word(word)
        xs[i][:][:] = encoded_word.flatten()
        ys[i][:][:] = encode_syllable_count(syllable_count)
    return xs, ys

