from data import DICTIONARY, LETTER_SCORES
import operator

def load_words():
    """Load dictionary into a list and return list"""

    word_list = []
    with open(DICTIONARY) as dict:
        for word in dict:
            word_list.append(word.strip('\n'))

    return word_list

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""

    value = 0
    for char in word.upper():
        if(str.isalpha(char)):
            value = value + LETTER_SCORES[char]
    return value

def max_word_value(word_list = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    # If no word list is specified load the dictionary
    if(word_list is None):
        word_list = load_words()

    best_word = ''
    best_score = 0

    # Check each word in the list for the best score
    for word in word_list:
        if(calc_word_value(word) > best_score):
            best_word,best_score = word,calc_word_value(word)

    return best_word
