"""
File: quadratic_solver.py
Name: Example Answer
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""
import math


def main():
    print('stanCode Quadratic Solver!')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))

    if a != 0:  # Restricts from variable "a" being zero

        discriminant = b * b - 4 * a * c

        if discriminant > 0:        # 2 roots
            root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print('Two roots: ' + str(root_1) + ', ' + str(root_2))

        elif discriminant == 0:     # 1 root
            root = -b / (2 * a)
            print('One root: ' + str(root))

        else:
            print('No real roots')

    else:
        print('The parameter \"a\" cannot be zero. Please start it over!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
