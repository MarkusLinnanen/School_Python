nameset = set({})
i = True
while i:
	iput = input("Enter a name: ")
	
	if not iput:
		i = False
		for x in nameset:
			print(x)
		break
	
	if nameset.issuperset(set((iput,))):
		print("Name input before!")
	else:
		print("New name!")
	nameset.add(iput)
	