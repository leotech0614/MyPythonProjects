"""
File: rocket.py
Name: leo HUNG
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This program draws a rocket and the size of rocket is determined by a constant defined as SIZE at top of the file.
    And the rocket can be divided into four parts: head, belt, upper, lower.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(' ', end='')
        for j in range(i+1):
            print('/', end='')
        for j in range(i+1):
            print('\\', end='')
        print('')


def belt():
    print('+', end='')
    for i in range(SIZE*2):
        print('=', end='')
    print('+')


def upper():
    for i in range(SIZE):
        print('|', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        for j in range(2*i+2):
            if j % 2 == 0:
                print('/', end='')
            else:
                print('\\', end='')
        for j in range(SIZE-1-i):
            print('.', end='')
        print('|', end='')
        print('')


def lower():
    for i in range(SIZE):
        print('|', end='')
        for j in range(i):
            print('.', end='')
        for j in range(-2*i+SIZE*2):
            if j % 2 == 0:
                print('\\', end='')
            else:
                print('/', end='')
        for j in range(i):
            print('.', end='')
        print('|', end='')
        print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
