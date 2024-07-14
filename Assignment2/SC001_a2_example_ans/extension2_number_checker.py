"""
File: extension2_number_checker.py
Name: Example Answer
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    This program checks whether the input number is a perfect, abundant, or deficient number.
    """
    print('Welcome to the number checker!')
    while True:
        n = int(input('n: '))
        if n == EXIT:
            break
        count = 0
        divided_num = 1
        while divided_num < n:
            if n % divided_num == 0:
                count += divided_num
            divided_num += 1
        if count == n:
            print(str(n) + ' is a perfect number')
        elif count < n:
            print(str(n) + ' is a deficient number')
        else:
            print(str(n) + ' is a abundant number')

    print('Have a good one!')


# DO NOT EDIT THE CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()