import geopy
import geopy.distance
import mysql.connector

cnx = mysql.connector.connect(user='userguy', password='pw0rd',
                              host='localhost', database='flight_game')
cursor = cnx.cursor(buffered = True)

def SearchAirport(ICAO1, ICAO2):
	geolocator = geopy.geocoders.Nominatim(user_agent="DatabaseDistance")
	
	query = ("SELECT latitude_deg, longitude_deg FROM airport "
			 "WHERE ident = %s or ident =  %s")
	
	
	cursor.execute(query, (ICAO1, ICAO2, ))
	t = ()
	
	for (latitude_deg, longitude_deg) in cursor:
		t += ((latitude_deg, longitude_deg),)
	
	print("Distance of airports: %8.3f" % (geopy.distance.distance(t[0], t[1]).km))

while True:
	iput1 = input("Input first airport ICAO code: ")
	iput2 = input("Input first airport ICAO code: ")
	
	if not (iput1 or iput2):
		print("Bye!")
		break
	else:
		SearchAirport(iput1, iput2)	

cursor.close()
cnx.close()