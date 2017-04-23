#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random
import itertools

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters():
    """Draw letters randomly up to the hand limit (NUM_LETTERS)"""

    return random.sample(POUCH, NUM_LETTERS)

def get_possible_dict_words():
    pass

def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""

    permu = [itertools.permutations(draw,i) for i in range(1,NUM_LETTERS + 1)]

    permu_list = []
    for p in permu:
       for t in p:
           permu_list.append(''.join(t))

    return permu_list

def _validation():
    pass


def main():
    l = _get_permutations_draw(draw_letters())
    print(l)
    #print(POUCH)

if __name__ == "__main__":
    main()
