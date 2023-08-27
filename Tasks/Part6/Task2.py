import random

def Throw(d = 6):
	return random.randint(1, d)

maxnum = int(input("Input amount of sides the dice has: "))
i = 1
while i % maxnum:
	i = Throw(maxnum)
	print(i)