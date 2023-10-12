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
validCommands = []
quitting = False

def MakeLocations(amount, diff, player):
	enemylocations = int(amount / 1.4 - (diff * 0.1))
	amountmade = 0
	enemytypes = ["light","heavy","boss"]
	query = "INSERT INTO locations VALUES (%s, %s, %s, %s, %s)"
	while amountmade < amount:
		cursor.execute("SELECT ident FROM airport WHERE type = 'airbase' AND ident NOT IN (SELECT location FROM game WHERE id = %s) ORDER BY RAND() LIMIT 1", (player, ))
		i = cursor.fetchall()[0][0]
		if amountmade < enemylocations:
			if amountmade == enemylocations - 1:
				cursor.execute(query, (amountmade, 0, i, enemytypes[-1], player))
			else:
				cursor.execute(query, (amountmade, 0, i, enemytypes[random.randint(0,1)], player))
		else:
			cursor.execute(query, (amountmade, 0, i, "abandoned", player))
		amountmade += 1
	cnx.commit()
	
def MakeGame(name, difficulty):
	cursor.execute("SELECT count(*) FROM game")
	playernum = cursor.fetchall()[0][0]
	cursor.execute("SELECT ident FROM airport WHERE type = 'airbase' ORDER BY RAND() LIMIT 1")
	location = cursor.fetchall()[0][0]
	query = "INSERT INTO game VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	hp = 100 * (1 - (.05 * difficulty))
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

def TextColorIterate(text = ["text"], it = 3, wait = 0.1, c = [Fore.RED, Fore.WHITE], sound = "", useClean = False, fillChar = " ", start = "", end = ""):
	if sound:
		playsound.playsound(sdir + sound, False)
	for i in range(it * len(c)):
		for t in text:
			print(start + c[i % len(c)] + t.center(80, fillChar) + end)
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
	

def CheckInput(IputList, OptionLists):
	for iput in IputList:
		if iput in OptionLists:
			return False
	return True

def CheckCommands(iput, OptionList):
	for option in OptionList
		if iput == option.name:
			return False
	return True

def getLocationsInRange():
	cursor.execute("SELECT airport_id, name, latitude_deg, longitude_deg FROM airport, locations WHERE game_id = %s AND airport_id = ident", (ID,))
	locations = cursor.fetchall()
	locationsInRange = []
	for l in locations:
		dist = geopy.distance.distance(gameLocation, (l[2], l[3])).km
		if dist < gameValues[3] * 3:
			locationsInRange.append([l[0], l[1], dist])
	return locationsInRange

def loadGame():
	cursor.execute("SELECT id, user_name, location, time FROM game")
	users = cursor.fetchall()
	idlist = []
	for (id, screen_name, location, time) in users:
		print(str(id) + ".",  "name: " + screen_name, "location: " + location,"Time played:" + str(time).split(".")[0])
		idlist.append(id)
	ID = input("which game would you like to continue, choose by number: ")
	while not ID.isnumeric() or CheckInput([int(ID)], idlist):
		print("input was invalid")
		ID = input("which game would you like to continue, choose by number: ")

def makeNew():
	gamename = input("What is Your Name: ")
	difficulty = input("Difficulty of the game as number 1-3: ")
	while not gamename.isalpha() or not gamename or not difficulty.isnumeric():
		print("Input was not sufficent")
		gamename = input("What is Your Name: ")
		difficulty = input("Difficulty of the game as number 1-3: ")
	ID = MakeGame(gamename, abs((int(difficulty) - 1) % 3))

def helpList():
	for cmd in validCommands: 
		print(f"Command: {cmd.name}, {cmd.desc}")
		
def move():
	validCommands = [cmd_exit]
	inRange = getLocationsInRange()
	airportVals = []
	ICAOs = []
	for vals in inRange:
		print(f"ICAO code: {vals[0]} \n" + f"Name: {vals[1]}\n" + f"Distance to: %.0f " % vals[2] + "km \n")
		ICAOs.append(vals[0].lower())

	choice = input("Input ICAO code of where you wanna move or exit or quit: ").lower()
	cbol = False
	while True:
		if CheckCommand(choice, validInputs):
			choice = input("Invalid input, Input ICAO code of where you want to move or 'exit' if you don't want to move: ").lower()
			cbol = True
		elif CheckInput(choice, ICAOs):
			choice = input("Invalid input, Input ICAO code of where you want to move or 'exit' if you don't want to move or 'quit' if you want to quit the game: ").lower()
		else:
			break
	if cbol:
		doCommands(choice)
		return
	else:
		for vals in inRange:
			if vals[0].lower() == choice:
				airportVals.extend(vals)
		cursor.execute("UPDATE game SET gas = gas - %s, location = %s WHERE id = %s", (int(airportVals[2] / 3), airportVals[0], ID))
		cursor.execute("UPDATE location SET location = 1 WHERE airport_id =  %s", (airportVals[0], ))
		cnx.commit()
		cursor.execute("SELECT * FROM game WHERE id = %s", (ID,))
		gameValues = cursor.fetchall()[0]
		if gameValues[2] > 100:
			cursor.execute("UPDATE game SET health = 100 WHERE id = %s", (ID,))
			gameValues[2] = 100
		
def Fight(enemyInfo):
	cursor.execute("SELECT enemy_count, type FROM enemy WHERE type IN (SELECT enemy_id FROM locations WHERE game_id = %s) ", (ID,))
	enemyInfo = cursor.fetchall()[0]
	if enemyInfo[0] > 6:
		enemyInfo[0] -= random.randint(0, 3)
	choice = input("'fight' to fight or 'evade' to evade").lower()
    hp -= enemyamount * enemytype * difficulty
    gas += 50 * enemyamount * enemytype - int(difficulty) * 3
    return gas, hp	
		
def doCommand(iput):
	for cmd in validCommands:
		if iput == cmd.name:
			cmd.action()
	
def q():
	TextColorIterate(["Bye!"], it = 50, wait = 0.02, c = [Fore.BLUE, Fore.GREEN, Fore.YELLOW], sound = "quit.wav", fillChar = " ", start = "\033[1m", end = "\033[0m")
	quitting = True

e = lambda : False
s = lambda : print(f"health: {gameValues[2]} \n" + f"gas: {gameValues[3]} \n" + f"xp: {gameValues[7]} \n" + f"ICAO location: {gameValues[2]}\n")

class Command:
	def __init__(self, name = "quit", desc = "quits the game", action = q):
		self.name = name
		self.desc = desc
		self.action = action

cmd_quit = Command()
cmd_exit = Command("exit", "Exit the current command", e)
cmd_load = Command("load", "Loads a previous game", loadGame)
cmd_new = Command("new", "Makes a new game", makeNew)
cmd_help = Command("help", "Lists all available commands and what they do", helpList)
cmd_stats = Command("status", "Prints current status of plane", s)
cmd_move = Command("move", "Lists airbases player can go to", move)
	
s = ["______ _ _       _     _     _    _               _      ",
"|  ___| (_)     | |   | |   | |  | |             | |     ",
"| |_  | |_  __ _| |__ | |_  | |  | |_ __ ___  ___| | __  ",
"|  _| | | |/ _` | '_ \| __| | |/\| | '__/ _ \/ __| |/ /  ",
"| |   | | | (_| | | | | |_  \  /\  / | |  __/ (__|   <   ",
"\_|   |_|_|\__, |_| |_|\__|  \/  \/|_|  \___|\___|_|\_\  ",
"            __/ |                                        ",
"           |___/                                         "]

TextColorIterate(s, 5, .075, useClean = True, sound = "hurt.wav")
	
TextColorIterate(text = ["StartMenu"], c = [Fore.BLUE, Fore.YELLOW], fillChar = "?", it = 5, wait = .1, sound = "hurt.wav", start = "\033[1m", end = "\033[0m") 

validCommands = [cmd_new, cmd_load, cmd_help, cmd_quit]

choice = input("Input: make 'new' game, 'load' previous game or 'quit', 'help' for commands: ").lower()
while CheckCommands(choice, validCommands):
	print("Input was insufficent")
	choice = input("Input: make 'new' game, 'load' previous game or 'quit', 'help' for commands: ").lower()
	
doCommand(choice, validCommands)

cursor.execute("SELECT * FROM game WHERE id = %s", (ID,))
gameValues = cursor.fetchall()[0]
cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (gameValues[1],))
gameLocation = cursor.fetchall()[0]
Clean()

startime = datetime.datetime.now()

validCommands = [cmd_help, cmd_quit, cmd_status, cmd_move]
while not quitting:
	if len(getLocationsInRange()) < 1:
		cursor.execute("UPDATE game SET gas = gas + 1000 WHERE id = %s", (ID,))
		cnx.commit()
		pass
	choice = input("What do you want to do? ").lower()
	while checkCommands(choice, validCommands):
		print("invalid input, input 'help' for commands")
		choice = input("What do you want to do? ").lower()
	doCommand(choice)
			
	
endtime = datetime.datetime.now() - startime
cursor.fetchall()
cursor.execute("UPDATE game SET time = ADDTIME(time,%s) WHERE id = %s", (endtime, ID))
cnx.commit()
cursor.close()
cnx.close()