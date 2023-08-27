i = "a"
l = []
while i:
	i = input("Input number: ")
	if i: l.append(int(i))
	
l.sort(reverse=True)
idex = 0
for x in l:
	if idex < 5: 
		print(l[idex])
		idex += 1
	