i = True
l = 10 * 10**60
h = 0
while i:
	#copied from last task
	iput = input("Enter a number: ")
	
	b = False
	
	for ch in iput:
		if ch.isalpha():
			b = True
			pass
	if not iput:
		print(f"highest was: {h}, lowest was: {l}")
		i = False
		break
	elif b:
		print("Input was not sufficent")
	else:
		iput = float(iput)
	
	if iput < l: l = iput
		
	if iput > h: h = iput
		