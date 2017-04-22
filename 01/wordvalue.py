from data import DICTIONARY, LETTER_SCORES
import operator

word_list = {}

with open(DICTIONARY) as dict:
    for word in dict:
        word_list[(word.strip('\n')).upper()] = 0

for word in word_list:
    value = 0
    for char in word:
        if(str.isalpha(char)):
            value = value + LETTER_SCORES[char]
    else:
        word_list[word] = value

word_list_sorted = sorted(word_list.items(), key=operator.itemgetter(1))
print(word_list_sorted)
