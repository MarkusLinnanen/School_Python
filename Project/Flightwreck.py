from colorama import Fore
import time as timemod
import os
import playsound
import keyboard
import mysql.connector
import random
import datetime
import geopy.distance

cnx = mysql.connector.connect(user='userguy', password='pw0rd',
                              host='localhost',
                              database='flightwreck')
cursor = cnx.cursor()

sdir = "/home/markus_l/Documents/School_Python/Project/Sounds/"

gameValues = ()
gameLocation = ()
ID = 0	
def MakeLocations(amount, diff, player):
	enemylocations = int(amount / 1.4 - (diff * 0.1))
	amountmade = 0
	query = "INSERT INTO locations VALUES (%s, %s, %s, %s, %s)"
	while amountmade < amount:
		cursor.execute("SELECT ident FROM airport WHERE type = 'airbase' AND ident NOT IN (SELECT location FROM game WHERE id = %s) ORDER BY RAND() LIMIT 1", (player, ))
		i = cursor.fetchall()[0][0]
		if amountmade < enemylocations:
			enemytypes = ["light","heavy","boss"]
			if amountmade == enemylocations - 1:
				cursor.execute(query, (amountmade, 0, i, enemytypes[-1], player))
			else:
				cursor.execute(query, (amountmade, 0, i, enemytypes[random.randint(0,1)], player))
		else:
			cursor.execute(query, (amountmade, 0, i, "abandoned", player))
		amountmade += 1
	cnx.commit()
	cursor.clear()
	
def MakeGame(name, difficulty):
	cursor.execute("SELECT count(*) FROM game")
	playernum = cursor.fetchall()[0][0]
	cursor.execute("SELECT ident FROM airport WHERE type = 'airbase' ORDER BY RAND() LIMIT 1")
	location = cursor.fetchall()[0][0]
	query = "INSERT INTO game VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
	hp = 100 * (1 + (.1 * difficulty))
	gas = 2400 - 100 * difficulty
	cursor.execute(query, (playernum, location, hp, gas, name, difficulty, 0, "NULL", '00:00:00'))
	cnx.commit()
	print(playernum)
	MakeLocations(100 + 30 * difficulty, difficulty, playernum)
	return playernum
	

def Clean():
	if os.name == 'nt':
		os.system('cls')

	else:
		os.system('clear')

Clean()

def TextColorIterate(text = ["text"], it = 3, wait = 0.1, c = [Fore.RED, Fore.WHITE], sound = "hurt.wav", useClean = False, fillChar = " "):
	playsound.playsound(sdir + sound)
	for i in range(it * len(c)):
		for t in text:
			print(c[i % len(c)] + t.center(80, fillChar))
		timemod.sleep(wait)
		if useClean:
			Clean()
		else:
			for t in text:
				print ("\033[A                             \033[A")
		
	for t in text:
		print(t.center(80, fillChar))
	print("\n")

def printhealth(condition = 10):
	s = "Health: "
	for i in range(10):
		if i < condition:
			s += "#"
		else:
			s += "X"
	print(Fore.GREEN + s.center(80))
	
def CheckANInput(IputList, OptionLists):
	for iput in IputList:
		if not iput.isalnum() or not iput:
			return False
		elif iput in OptionLists[IputList.index(iput)]:
			return True
		return False

def getLocationsInRange():
	cursor.execute("SELECT airport_id, latitude_deg, longitude_deg FROM airport, locations WHERE game_id = %s AND airport_id = ident", (ID,))
	locations = cursor.fetchall()
	locationsInRange = []
	for l in locations:
		if geopy.distance.distance(gameLocation, (l[1], l[2])).km > gameValues[3] * 3:
			locationsInRange.append(l[0])
	return locationsInRange

s = ["______ _ _       _     _     _    _               _      ",
"|  ___| (_)     | |   | |   | |  | |             | |     ",
"| |_  | |_  __ _| |__ | |_  | |  | |_ __ ___  ___| | __  ",
"|  _| | | |/ _` | '_ \| __| | |/\| | '__/ _ \/ __| |/ /  ",
"| |   | | | (_| | | | | |_  \  /\  / | |  __/ (__|   <   ",
"\_|   |_|_|\__, |_| |_|\__|  \/  \/|_|  \___|\___|_|\_\  ",
"            __/ |                                        ",
"           |___/                                         "]

TextColorIterate(s, 5, .075, useClean = True)
	
TextColorIterate(text = ["Make new or load"], c = [Fore.WHITE], fillChar = "?", it = 0) 

choice = input("'new' for new game, 'load' to load game: ").lower()
while not CheckANInput([choice], [["new", "load"]]):
	print("Input was insufficent")
	choice = input("'new' for new game, 'load' to load game: ").lower()

if choice == "new":
	gamename = input("What is Your Name: ")
	difficulty = input("Difficulty of the game as number 1-3: ")
	while (not gamename.isalnum() or not gamename) and not difficulty.isnumeric():
		print("Input was not sufficent")
		gamename = input("What is Your Name: ")
		difficulty = input("Difficulty of the game as number 1-3: ")
	ID = MakeGame(gamename, abs((int(difficulty) - 1) % 3))
else:
	cursor.execute("SELECT id, user_name, location, time FROM game")
	users = cursor.fetchall()
	idlist = []
	for (id, screen_name, location, time) in users:
		print(str(id) + ".",  "name: " + screen_name, "location: " + location,"Time played:" + str(time).split(".")[0])
		idlist.append(id)
	ID = input("which game would you like to continue, choose by number: ")
	while not ID.isnumeric() or int(ID) not in idlist or not ID:
		print("input was invalid")
		ID = input("which game would you like to continue, choose by number: ")

cursor.execute("SELECT * FROM game WHERE id = %s", (ID,))
gameValues = cursor.fetchall()[0]
cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (gameValues[1],))
gameLocation = cursor.fetchall()[0]
Clean()
startime = datetime.datetime.now()
alwaysInputs = [["quit", "quits the game"], ["help", "lists current commands"]]
dClose = 1
while(dClose):
	inRange = getLocationsInRange()
	validInputs = alwaysInputs + [["Move", "Lists the locations you can currently go to and takes ICAO code as input"]]
	choice = input("What do you want to do? ").lower()
	validCommands = []
	for i in validInputs:
		validCommands.append(i[0])
	while not CheckANInput([choice], validCommands):
		print("invalid input, input 'help' for commands")
		choice = input("What do you want to do? ").lower()
	if choice == "help":
		for v in validInputs:
			print("command: " + v[0] + ", desc: " + v[1])
	elif choice == "quit":
		dClose = 0
		break
		
	
	
endtime = datetime.datetime.now() - startime
cursor.fetchall()
cursor.execute("UPDATE game SET time = ADDTIME(time,%s) WHERE id = %s", (endtime, ID))
cnx.commit()
cursor.close()
cnx.close()