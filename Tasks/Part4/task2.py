i = 0
while i < 1:
	iput = input("Input cm to make inch: ")
	
	b = False
	
	for ch in iput:
		if ch.isalpha():
			b = True
			pass
	
	
	if b or float(iput) < 0:
		print("Input was inadequate")
		i += 1
	else:
		print(iput * 2.54)