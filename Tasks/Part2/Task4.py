import statistics # for statistics.mean()

# used Task3's modified function
def InputNum():
	v = input("Input integer: ")
	if v.isnumeric():
		return int(v)
	else:
		print("Input was not numeric")
		return InputNum()


def InputNumArr():
	print("Input 3 numbers")
	a = []
	for x in range(3):
		i = InputNum()
		a.append(i)
	
	return a
	
	
arr = InputNumArr()

print("Sum of the numbers: ", sum(arr))
print("The numbers timed by each other: ", arr[0] * arr[1] * arr[2])
print("Average of the number: ", statistics.mean(arr))