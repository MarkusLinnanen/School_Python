# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
	conn = mariadb.connect(
		user="userguy",
        password="pw0rd",
		host="localhost",
		port=1125,
		database="flight_game"

    )
except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)

def SearchAirport(ICAO):
	cur = conn.cursor()
	cur.execute("SELECT name, municipality FROM airport WHERE ident=?", (ICAO,))
	for (name, municipality) in cur:
		print(name + ", " + municipality)

while True:
	iput = input("Input airport ICAO code: ")
	
	if not iput:
		print("Bye!")
		break
	else:
		SearchAirport(iput)