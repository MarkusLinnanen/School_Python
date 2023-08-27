b = True
while b:
	num = int(input("Enter number: "))
	l = []
	i = 1
	for i in range(num):
		if not (num % i): l.append(i)
		i += 1
		
	if len(l) == 2:
		print("Number is prime number")
	else:
		print("Number is not prime number")
		
		