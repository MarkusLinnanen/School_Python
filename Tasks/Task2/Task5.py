# Modified Task4's modified function
# The code is somewhat cluttered and somewhat complex for convenience

# Other options didn't work so made my own function, needs more work because a empty enter crashes
def CheckForAlpha(s):
	for chr in s:
		if chr.isalpha():
			return True
			
	return False

# Needed some work but this is where we get the amount of grams the object is, could be done better
def SumArray(arr, x, v):
	for i in range(x):
		v *= arr[i]
	
	return v
	

# Used two arrays in a honestly stupid way to get the results knew there were easier solutions
def InputValue(x, s):

	i = [13.3, 32, 20]
	v = input("\n" + "Input amount of " + s + ": \n")
	
	if CheckForAlpha(v):
		print("Input was not numeric")
		return InputValue(x, s)
	#else here is useless but added anyway
	else:
		return SumArray(i, 3 - x, abs(float(v)))


def InputNums():
	a = ["Talents", "Nails", "Bullets"]
	f = 0.0
	for x in range(3):
		f += InputValue(x, a[x])
			
	return f
	
	
kilograms = InputNums() 
grams = (kilograms % 1000)

print("\n" + "Mass by current parameters:")
print(int(kilograms // 1000), "kg and", round(grams, 5), "g")
