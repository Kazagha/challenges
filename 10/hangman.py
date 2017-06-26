from string import ascii_lowercase
import sys

from movies import get_movie as get_word  # keep interface generic
from graphics import hang_graphics

ASCII = list(ascii_lowercase)
HANG_GRAPHICS = list(hang_graphics())
ALLOWED_GUESSES = len(HANG_GRAPHICS)
PLACEHOLDER = '_'


class Hangman(object):

    def __init__(self, word):
        self.word = word

    def game(self):

        guess_num = 0

        while (guess_num < ALLOWED_GUESSES):
            print(HANG_GRAPHICS[guess_num])

            input('Input letter: ')
            guess_num = guess_num + 1
        else:
            print(f'You have died... the word was {self.word}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    print(word)

    # init / call program
    h = Hangman(word)
    h.game()
