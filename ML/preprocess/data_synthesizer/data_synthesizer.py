import os
import json
import random
from segment import dict_words

base = dict_words()
MAX_SYLLABLE_LEN = 14
NUM_OF_CLASSES = MAX_SYLLABLE_LEN + 1  # add zero syllables as a class


def get_num_of_words_to_create_per_class():
    """
    It calculates the number of words needed to be calculated per class.
    returns num_of_words_to_create_list: should be list[int]
    """
    MIN_PER_SAMPLE = 50000
    num_of_words_to_create_list = [0 for _ in range(NUM_OF_CLASSES)]
    for i in range(NUM_OF_CLASSES):
        if i > 3:
            num_of_base = len(base[i])
            if num_of_base < MIN_PER_SAMPLE:
                num_of_words_to_create = MIN_PER_SAMPLE - num_of_base
                num_of_words_to_create_list[i] = num_of_words_to_create
    return num_of_words_to_create_list


def get_rand_base_word_of_len(syll_len):
    """
    It randomly chooses a random base word of the given length.
    syll_len: syllable length of the desired random base word, should be an int
    returns random base word of the given length, should be string
    """
    return random.choice(base[syll_len])


def synthesize_long_word(syll_len):
    """
    It synthesizes a long word (<= 4 syllables).
    syll_len: syllable length of the desired synthesize word, should be int
    return synthetic_word, should be string
    """
    if syll_len < 4:
        print("words must be > 4 sylls to be synthesized")
    elif 4 <= syll_len <= MAX_SYLLABLE_LEN:
        synthetic_word = get_rand_base_word_of_len(3)
        for _ in range(0, syll_len - 3):
            synthetic_word += get_rand_base_word_of_len(1)
        print(synthetic_word)
        return synthetic_word
    else:
        print("words must be <= 14 sylls to be synthesized")


def create_synthesized_word_mat(num_of_words_to_create_list):
    """
    It synthesizes the number of words need and stores them in a list[list]
    according to their syllable length.
    num_of_words_to_create_list: number of words needed per class,
                                 should be list[int]
    returns synthesized_mat: list of list of words, 
                            should be list[list[string]]
                            where synthesized_mat[i] has list of 
                            word with syllable length of i
    """
    synthesized_mat = base.copy()
    for i, num_to_create in enumerate(num_of_words_to_create_list):
        if i > 3:
            for _ in range(num_to_create):
                synthesized_mat[i].append(synthesize_long_word(i))
    return synthesized_mat


def create_synthesized_dict(synthesized_mat):
    """
    It converts synthezised_mat[i][j] into synthesized_dict[j]: i.
    synthesized_mat: list of list of words, should be list[list[string]]
                     where synthesized_mat[i] has list of 
                     word with syllable length of i
    returns synthesized_dict, should be dict with key:string and value:int.
    """
    synthesized_dict = {}
    for i, synth_words in enumerate(synthesized_mat):
        for synth_word in synth_words:
            synthesized_dict[synth_word] = i
    return synthesized_dict


num_of_words_to_create_list = get_num_of_words_to_create_per_class()
synthesized_mat = create_synthesized_word_mat(num_of_words_to_create_list)
sythezised_dict = create_synthesized_dict(synthesized_mat)
OUTPUT_DATA_PATH = f"{os.getcwd()}/data/synthetic_data/synthetic_dict.json"
with open(OUTPUT_DATA_PATH, "w") as file:
    json.dump(sythezised_dict, file)
