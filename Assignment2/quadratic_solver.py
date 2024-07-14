"""
File: quadratic_solver.py
Name:
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
	"""
	This program helps we find the roots of quadratic function
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	Discriminant = b * b - 4 * a * c
	if Discriminant > 0:
		print('Two real Roots: '+ str((-b)/(2*a) + math.sqrt(Discriminant)/(2*a)) + ', ' + str((-b)/(2*a) - math.sqrt(Discriminant)/(2*a)))
	elif Discriminant == 0:
		print('One real Roots: ' + str((-b)/(2*a) + math.sqrt(Discriminant)/(2*a)))
	else:
		print('No real Roots!')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
