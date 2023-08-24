# using function to recursively call in case the input was not numeric
def InputRadius():
	r = input("input radius: ")
	if r.isnumeric():
		return float(r)
	else:
		print("Was not numeric")
		return InputRadius()
	

radius = InputRadius()

print(3.14 * radius**2)