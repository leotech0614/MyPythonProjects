"""
File: prime_checker.py
Name: Example Answer
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. At the beginning, ” Welcome to the prime checker” is printed on Console.
And the program will ask the user to enter an integer that 
is greater than 1 and checks if it is a prime number.
The program ends when the user enter the Exit number.
"""

EXIT = -100


def main():
	print('Welcome to the prime checker')
	while True :
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break
		else:
			if is_prime(n):
				print(str(n) + ' is a prime number.')
			else :
				print(str(n) + ' is not a prime number.')


def is_prime(n):
	"""
	: param n: int, an integer that is greater than 1
	: return : bool, True if n is a prime number; False if n is not a prime number
	"""
	for i in range(2, n, 1):
		if n % i == 0:
			return False
	return True


	# Below is the fastest way of doing it

	# for i in range(2, int(n ** 0.5) + 1, 1) :
	# 	if n % i == 0 :
	# 		return False
	# return True


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
