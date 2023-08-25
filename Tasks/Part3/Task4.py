while True:
	year = int(input("Input a year: "))
	if (year % 4 == 0 and year % 100 == 0 and year % 400 != 0) or year % 4:
		print(year, "is not a leap year")
	else:
		print(year, "is a leap year")

#Wanted to do this task in as little amount of code as i could quickly make
#Obviously can break with a string input