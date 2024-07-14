"""
File: prime_checker.py
Name:
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -100  #Sentinel value


def main():
	"""
	The program will continually checks if it is a prime number.
	"""
	print('Welcome to the prime checker!(or -100 to quit)')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!!')
			break
		else:
			# n/1,2,3,...,n-1,n and only 1,n are divisible.
			if n == 2:
				print(str(n) + ' is a prime number.')
			else:
				n1 = n - 1
				while True:
					if n % n1 != 0:
						n1 = n1 - 1
					elif n1 != 1:
						# Apart from 1, there are other numbers that can be divided evenly.
						print(str(n) + ' is not a prime number.')
						break
					else:
						# only 1 is divisible.
						print(str(n) + ' is a prime number.')
						break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
