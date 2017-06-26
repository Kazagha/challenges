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
        self.guess_chars = []

        # Add any non-alpha characters to the list automatically
        for char in word.lower():
            if(char not in ASCII):
                self.guess_chars.append(char)

    def game(self):

        #guess_chars = []
        wrong_guess_count = 0

        while (wrong_guess_count < ALLOWED_GUESSES):
            print(HANG_GRAPHICS[wrong_guess_count])

            # Remove unknown letters from the word
            word_clue = word
            for char in ASCII:
                if char not in self.guess_chars:
                    word_clue = word_clue.lower().replace(char, PLACEHOLDER)

            print(f'{word_clue}')

            # Prompt the user for a guess, add it to the array
            self.guess_chars.append(input('Input letter: ').lower())

            # Check if the guess is correct
            if(self.guess_chars[-1] in (char.lower() for char in word)):
                print(f'You guessed correctly')

                # Check if all the characters in the word have been guessed
                if(len({char for char in self.guess_chars if char in word.lower()}) == len(set(word.lower()))):
                    # All characters have been guessed, end the game
                    print(f'The word is {word}!')
                    break
            else:
                # Incorrect guess, increment the count
                print(f'There is no {self.guess_chars[-1].upper()}, try again')
                wrong_guess_count = wrong_guess_count + 1

        else:
            print(f'You have died... the word was {self.word}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        word = sys.argv[1]
    else:
        word = get_word()
    #print(word)

    h = Hangman(word)
    h.game()
