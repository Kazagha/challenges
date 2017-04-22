from data import DICTIONARY, LETTER_SCORES
import operator

def load_words():
    """Load dictionary into a list and return list"""
    word_list = []
    with open(DICTIONARY) as dict:
        for word in dict:
            #word_list[(word.strip('\n')).upper()] = 0
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

def max_word_value():
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    pass

lst = load_words()
calc_word_value('bob')

word_list = {}
for word in word_list:
    value = 0
    for char in word:
        if(str.isalpha(char)):
            value = value + LETTER_SCORES[char]
    else:
        word_list[word] = value

word_list_sorted = sorted(word_list.items(), key=operator.itemgetter(1))
print(word_list_sorted)
