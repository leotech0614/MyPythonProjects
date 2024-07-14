"""
File: extension4_narcissistic_checker.py
Name: Example Answer
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    This program checks whether the input number is a narcissistic number.
    """
    print('Welcome to the narcissistic number checker!')
    while True:
        number = int(input('n: '))
        if number == EXIT:
            break
        else:
            # check number's length
            length = 0
            current = number
            while current > 0:
                current //= 10
                length += 1

            # process the number
            total = 0
            current = number
            while current > 0:
                unit = current % 10
                total += unit**length
                current = (current - unit)//10

            if total == number:
                print(str(number) + ' is a narcissistic number')
            else :
                print(str(number) + ' is not a narcissistic number')

    print('Have a good one!')




# DO NOT EDIT THE CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()