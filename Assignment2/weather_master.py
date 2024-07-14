"""
File: weather_master.py
Name:
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100  #Sentinel value

def main():
	"""
	This program is a weather analyzer, ended by entering -100.
	It will help us to find the average, highest, lowest and cold days(<16'C) among the inputs.
	"""
	print('stanCode \"Weather 4.0\"!')
	data = int(input('Next Temperture (or ' + str(EXIT) + ' to quit): '))
	if data == EXIT:
		print('No temperature were entered!')
	else:
		maximum = data
		minimum = data
		datas = data
		number = 0
		if data < 16:
			cold_days = 1
		else:
			cold_days = 0
		while True:
			data = int(input('Next Temperture (or ' + str(EXIT) + ' to quit): '))
			number = number + 1
			average = datas / number
			if data == EXIT:
				break
			else:
				datas = datas + data  # This helps us know all the sum of datas.
				if data > maximum:
					maximum = data
				if data < minimum:
					minimum = data
				if data < 16:
					cold_days = cold_days + 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold_days) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
