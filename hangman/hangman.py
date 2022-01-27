import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()                                #what the user has guessed

    lives = 6
    
    while len(word_letters) > 0:
        print('You have {} lives left and You have used these letters: {}' .format(lives, ' '.join(used_letters)))
        
        if lives == 0:
            break

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            elif user_letter not in word_letters:
                lives = lives -1
        
        elif user_letter in used_letters:
            print('You have already used that character. Please try again')
        
        else:
            print('Invalid character. Please try again.')

hangman()
