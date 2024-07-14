"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program computes Hailstone sequences and it will also count how many steps to reach 1.
    """
    print('This program computes Hailstone sequences.')
    print(' ')
    n = int(input('Enter a number: '))
    number = 0
    while True:
        if n == 1:
            break
        else:
            number = number + 1
            if n % 2 == 0:
                print(str(n) + ' is an even, so I take half: ' + str(int(n/2)))
                n = int(n/2)
            else:
                print(str(n) + ' is an odd, so I make 3n+1: ' + str(int(3*n + 1)))
                n = int(3*n + 1)
        # if n % 2 == 0:
        #     print(str(n) + ' is an even, so I take half: ' + str(int(n/2)))
        #     n = int(n/2)
        #     number = number + 1
        # else:
        #     print(str(n) + ' is an odd, so I make 3n+1: '+ str(int(3*n + 1)))
        #     n = int(3*n + 1)
        #     number = number + 1
    print('It took ' + str(number) + ' steps to reach 1.')








# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
