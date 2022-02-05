import json
import numpy as np

NUM_OF_WORDS = 657084
MAX_WORD_LEN = 125
DIMS = 8
NB_CLASSES = 15


def is_a_consonant(char):
    consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "z",
    ]
    return char in consonants


def is_a_semivowel(char):
    semivowels = ["y", "w"]
    return char in semivowels


def is_a_vowel(char):
    vowels = ["a", "e", "i", "o", "u"]
    return char in vowels


def encode_vowel(vowel):
    vowel_char_type = [1, 0, 0]
    vowel_dict = {
        "a": [1, 0, 0, 0, 0],
        "e": [0, 1, 0, 0, 0],
        "i": [0, 0, 1, 0, 0],
        "o": [0, 0, 0, 1, 0],
        "u": [0, 0, 0, 0, 1],
    }
    return np.array(vowel_char_type + vowel_dict[vowel]).astype(int)


def encode_semivowel(semivowel):
    semivowel_char_type = [1, 1, 0]
    semivowel_dict = {"y": [0, 0, 1, 0, 0], "w": [0, 0, 0, 0, 1]}
    return np.array(semivowel_char_type + semivowel_dict[semivowel]).astype(int)


def encode_consonant(consonant):
    consonant_char_type = [0, 1, 0]
    zero_pad = [0, 0, 0, 0, 0]
    return np.array(consonant_char_type + zero_pad).astype(int)


def encode_other_char(other_char):
    other_char_type = [0, 0, 1]
    zero_pad = [0, 0, 0, 0, 0]
    return np.array(other_char_type + zero_pad).astype(int)


def encode_char(char):
    if is_a_vowel(char):
        return encode_vowel(char)
    elif is_a_semivowel(char):
        return encode_semivowel(char)
    elif is_a_consonant(char):
        return encode_consonant(char)
    else:
        return encode_other_char(char)


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

