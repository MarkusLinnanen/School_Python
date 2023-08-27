import random

def SumList(l):
	total = 0
	for i in range(len(l)):
		total += l[i]
	return total

mylist = [random.randint(0, 50), random.randint(0, 50)]
print(SumList(mylist))