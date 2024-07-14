"""
File: hangman.py
Name: leo HUNG
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program is a hangman game, we can input the alphabet and the program will tell us if we have the right answer.
    We have N_TURNS time to guess the answer or we will be hang :( .
    """
    N_TURNS = 7
    word1 = random_word()
    word2 = random_word1(word1)  # Turn the random word to dash
    print('The words looks like: ' + word2)
    while True:
        print('You have ' + str(N_TURNS) + ' wrong guesses left.')
        # We'll first determine whether the input string is correct
        while True:
            s = input('Your guess: ')
            if not s.isalpha():
                print('Illegal format')
            else:
                if len(s) > 1:
                    print('Illegal format')
                else:
                    ans = ''
                    if s.islower():
                        ans = ans + s.upper()
                        break
                    else:
                        ans = ans + s
                        break
        s = ans
        # If it's correct, then we'll determine if it's within 'word1
        if word1.find(s) != -1:
                print('You are correct!')
                word2 = tracking(word1, word2, s)
                if word1 == word2:
                    print('You win!')
                    print('The answer is ' + str(word1))
                    break
                else:
                    print('The word looks like: ' + word2)
        elif N_TURNS == 1:
            print('There is no ' + s + '\'s' + ' in the word')
            print('You are completely hung :( ')
            print('The answer is ' + str(word1))
            break
        else:
            N_TURNS = N_TURNS - 1
            print('There is no ' + s + '\'s' + ' in the word')


def tracking(word1,word2,s):
    """
    This will re-build word2 according to word1 and s which we input.
    """
    ans = ''
    for i in range(len(word1)):
        if word1[i] == s:
            first_part = word2[:i]
            second_part = word2[(i+1):]
            ans = first_part + s + second_part
            word2 = ans
    return word2


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


def random_word1(word1):
    """
    THis will turn the alphabet to dash.
    """
    word2 = ''
    for i in range(len(word1)):
        word2 = word2 + '-'
    return word2


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
