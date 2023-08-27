i = 0
while i < 5:
	print("Input Username and Password")
	usrni = input("Username: ")
	passwi = input("Password: ")
	
	if usrni == "python" and passwi == "rules":
		print("Welcome!")
		i = 5
	else:
		print("Username or Password incorrect \n")
		i += 1
		if i == 5: 	print("Entry denied!")
