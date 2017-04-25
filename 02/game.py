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

def get_possible_dict_words(draw):
    """ Return a list of all possible dictionary words given the specified draw 
                
    Checks each permutation against the dictionary
    """

    perm_words = [''.join(word).lower() for word in _get_permutations_draw(draw)]

    return set(perm_words) & set(DICTIONARY)

def _get_permutations_draw(draw):
    """Helper for get_possible_dict_words to get all permutations of draw letters.
    Hint: use itertools.permutations"""

    #permu = [itertools.permutations(draw,i) for i in range(1,NUM_LETTERS + 1)]

    for i in range(1, NUM_LETTERS + 1):
        yield from list(itertools.permutations(draw,i))

def input_word(draw):
    """Ask player for a word and validate against draw.
    Use _validation(word, draw) helper."""

    player_word = input('Enter your word: ')
    if _validation(player_word, draw):
        print(f'Your word {player_word} scored {calc_word_value(word=player_word)} points')
    else:
        print(f'You have entered an invalid word')

def _validation(word, draw):
    """Validations: 1) only use letters of draw, 2) valid dictionary word"""


    for char in word.upper():
        if char in draw:
            draw.remove(char)
        else:
            raise ValueError

    if word.lower() not in DICTIONARY:
        print(word)
        raise ValueError

    return word


def main():
    draw = draw_letters()
    print(f'Drawing hand: {draw}')
    input_word(draw)

    best_word = max_word_value(get_possible_dict_words(draw))
    print(f'The best possible word is {best_word} with a score of {calc_word_value(best_word)}')


if __name__ == "__main__":
    main()
