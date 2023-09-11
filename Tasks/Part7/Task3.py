print("Welcome to the airport system")
airportdict = {}

def InputAirport():
	IICAO = input("Input ICAO code: ")
	airportname = input("Input airport name: ")
	airportdict[IICAO] = airportname

def SearchAirport():
	SICAO = input("Input airport ICAO code: ")
	print(airportdict[SICAO])


funcs = [InputAirport, SearchAirport]
while True:
	iput = int(input("1 for Input, 2 for Search, 3 for Exit: "))
	
	if iput == 3:
		print("Bye!")
		break
	elif iput < 1 or iput > 2:
		print("input was insufficient")
		pass
	else:
		funcs[iput - 1]()
	