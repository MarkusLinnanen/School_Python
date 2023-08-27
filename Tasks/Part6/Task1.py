import random

def Throw():
	return random.randint(1, 6)

i = 1
while i % 6:
	i = Throw()
	print(i)