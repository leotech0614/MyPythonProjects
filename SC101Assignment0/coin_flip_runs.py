"""
File: coin_flip_runs.py
Name: leo HUNG
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random


def main():
	"""
	We can input a number to represent how many times a coin with identical sides will be tossed.
	The system will then randomly toss the coin and print out the tossing process.
	"""
	print('Let\'s filp a coin!' )
	n = int(input('Number of runs: '))
	num_run = 0
	r1_r2_same = False  # Use this as a switch.

	r1 = random.randrange(1, 3)
	if r1 == 1:
		print('H', end='')
	else:
		print('T', end='')

	while True:
		r2 = random.randrange(1, 3)
		if r2 == 1:
			print('H', end='')
		else:
			print('T', end='')

		if r1 == r2:  # Check for continuity in addition to matching at the front and back.
			if not r1_r2_same:
				num_run += 1
				r1_r2_same = True
		else:
			r1_r2_same = False
		r1 = r2

		if num_run == n:
			break

# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
