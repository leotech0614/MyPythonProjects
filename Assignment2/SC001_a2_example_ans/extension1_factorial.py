"""
File: extension1_factioral.py
Name: Example Answer
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = 100


def main():
    """
    This program calculates the factorial of inputted numbers
    """
    print('Welcome to stanCode factorial master!')
    while True :
        n = int(input('Give me a number, and I will list the answer of factorial: '))
        if n == EXIT:
            break
        else:
            count = 1
            ans = 1
            while n != count:
                count += 1
                ans *= count
            print('Answer: ' + str(ans))
    print('------See ya!------')


# DO NOT EDIT THE CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
