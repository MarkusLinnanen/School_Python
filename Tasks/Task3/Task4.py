while True:
	year = int(input("Input a year: "))
	if(year % 4 or (year % 100 and year % 400)):
		print(year, "is not a leap year")
	else:
		print(year, "is a leap year")

#Wanted to do this task in as little amount of code as i could quickly make
#Obviously can break with a string input