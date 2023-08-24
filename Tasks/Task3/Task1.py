def InputCod():
	l = input("Input cod lenght: ")
	for chr in l:
		if chr.isalpha():
			return InputCod()
			
	return float(l)

lenght = InputCod()

if(lenght < 37):
	print("Let the fish go it's", 37 - lenght, "under the allowed lenght")

