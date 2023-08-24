i = 0

while i < 1:
	gender = input("Input gender: ")
	hemoglobin = input("Input hemoglobin value: ")
	
	hemobool = False
	
	for ch in hemoglobin:
		if ch.isalpha():
			hemobool = True
			pass
			
	if hemobool:
		print("Hemoglobin is inadequate")
		pass
	else:
		hemoglobin = int(hemoglobin)
			

	hquality = ["Low", "High", "Normal"]

	if gender.lower() == "male":
		if hemoglobin < 134:
			print("your hemoglobin is " + hquality[0])
		elif hemoglobin > 195:
			print("your hemoglobin is " + hquality[1])
		else:
			print("your hemoglobin is " + hquality[2])
		i += 1	
		
	elif gender.lower() == "female":
		if hemoglobin < 117:
			print("your hemoglobin is " + hquality[0])
		elif hemoglobin > 175:
			print("your hemoglobin is " + hquality[1])
		else:
			print("your hemoglobin is " + hquality[2])
		i += 1
		
	else:
		print("Gender is inadequate")		