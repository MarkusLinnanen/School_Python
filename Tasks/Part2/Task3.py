#Modified Task2's InputRadius function for a more modular use
def InputNumVar(s):
	v = input("input " +s+ ": ")
	if v.isnumeric():
		return float(v)
	else:
		print("Input was not numeric")
		return InputNumVar(s)
	
print("Input parameters for square in cm")
height = InputNumVar("height")
lenght = InputNumVar("lenght")

print("Perimeter of the square is " + str((height + lenght) * 2) + " cm \n")
print("Area of the square is " + str(height * lenght) + " cm²")