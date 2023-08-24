#cabinclass = ["LUX", "A", "B", "C"]

#i = input("Input Cabin Class, 0 for LUX, 1 for A, 2 for B, 3 for C: ")

#while not i.isnumeric():
#	i = input("Input Cabin Class, 0 for LUX, 1 for A, 2 for B, 3 for C: ")

#i = int(i)
#i = i % 4
#print(cabinclass[i])

cabinclass = ["LUX", "A", "B", "C"]

i = input("Input Cabin Class, LUX, A, B or C: ")

#Can be broken with input of L or LU
#Essentially anything that is in the array but not in if statement
if i.upper() not in cabinclass:
	print("Insufficient cabin class")
	i = input("Input Cabin Class, LUX, A, B or C: ")
elif i.upper() == cabinclass[0]:
	print("LUX is a cabin with a terrace on the top deck")
elif i.upper() == cabinclass[1]:
	print("A is a windowed cabin above the car deck")
elif i.upper() == cabinclass[2]:
	print("B is a non-windowed cabin above the car deck")
elif i.upper() == cabinclass[3]:
	print("C is a windowed cabin below the car deck")
else:
	print("You found an error, well done")