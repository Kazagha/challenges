from data import DICTIONARY, LETTER_SCORES

word_list = []

with open(DICTIONARY) as dict:
    for word in dict:
        word_list.append(word.strip("\n"))

print(word_list)
