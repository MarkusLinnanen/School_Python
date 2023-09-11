import mysql.connector

cnx = mysql.connector.connect(user='userguy', password='pw0rd',
                              host='localhost',
                              database='flight_game')
cursor = cnx.cursor()

def GetTypeAmount(ISO):
	query = ("SELECT type, count(type) as count FROM airport "
			 "WHERE iso_country = %s "
			 "group by type")

	cursor.execute(query, (ISO,))

	for (type, count) in cursor:
		print(type + ",", count,)
	
	print("\n")

while True:
	iput = input("Input airport ISO: ")
	
	if not iput:
		print("Bye!")
		break
	else:
		GetTypeAmount(iput)	
	
cursor.close()
cnx.close()