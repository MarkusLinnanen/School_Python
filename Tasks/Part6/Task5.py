def OnlyEven(l):
	evenl = []
	for i in range(len(l)):
		if not (l[i] % 2): evenl.append(l[i])
	return evenl

mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
myevenlist = OnlyEven(mylist)
print("Original List:", mylist)
print("Even List:", myevenlist) 