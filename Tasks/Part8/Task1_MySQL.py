import mysql.connector

cnx = mysql.connector.connect(user='userguy', password='pw0rd',
                              host='localhost',
                              database='flight_game')
cursor = cnx.cursor()

def SearchAirport(ICAO):
	query = ("SELECT name, municipality FROM airport "
			 "WHERE ident = %s")

	cursor.execute(query, (ICAO,))

	for (name, municipality) in cursor:
		print(name + ",", municipality)

while True:
	iput = input("Input airport ICAO code: ")
	
	if not iput:
		print("Bye!")
		break
	else:
		SearchAirport(iput)	
	
cursor.close()
cnx.close()