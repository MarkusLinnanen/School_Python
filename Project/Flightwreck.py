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

def checkHealth():
	global ID
	cursor.execute("SELECT * FROM game WHERE id = %s", (ID,))
	gameValues = cursor.fetchone()
	if gameValues[2] > 100:
		cursor.execute("UPDATE game SET health = 100 WHERE id = %s", (ID,))
		gameValues[2] = 100
		cnx.commit()
	elif gameValues[2] <= 0:
		TextColorIterate(["Your plane was destroyed and you died!"], 10, 0.1, [Fore.YELLOW, Fore.RED, Fore.BLACK], "explosion.wav", False, "!", "\033[1m", "\033[0m")

	
def printhealth():
	s = "Health: "
	for i in range(10):
		if i < condition:
			s += "#"
		else:
			s += "X"
	print(Fore.GREEN + "Health: " + s + "\033[0m")
	

def CheckInput(iput, OptionLists):
	if iput in OptionLists:
		return False
	return True

def CheckCommands(iput):
	for option in validCommands:
		if iput == option.name:
			option.action()
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
	global ID
	cursor.execute("SELECT id, user_name, location, time FROM game")
	users = cursor.fetchall()
	idlist = []
	for (id, screen_name, location, time) in users:
		print(str(id) + ".",  "name: " + screen_name, "location: " + location,"Time played:" + str(time).split(".")[0])
		idlist.append(id)
	ID = input("which game would you like to continue, choose by number: ")
	while not ID.isnumeric() or CheckInput(int(ID), idlist):
		print("input was invalid")
		ID = input("which game would you like to continue, choose by number: ")

def makeNew():
	global ID
	gamename = input("What is Your Name: ")
	difficulty = input("Difficulty of the game as number 1-3: ")
	while not gamename.isalpha() or not gamename or not difficulty.isnumeric():
		print("Input was not sufficent")
		gamename = input("What is Your Name: ")
		difficulty = input("Difficulty of the game as number 1-3: ")
	ID = MakeGame(gamename, abs((int(difficulty) - 1) % 3))
	
def deleteGame():
	global ID
	cursor.execute("DELETE game WHERE id = %s", (ID,))
	cursor.execute("UPDATE game, locations SET id = id - 1 WHERE id > %s", (ID,))
	cursor.execute("UPDATE locations SET game_id = game_id - 1 WHERE game_id > %s", (ID,))
	cnx.commit

def helpList():
	for cmd in validCommands: 
		print(f"Command: {cmd.name}, {cmd.desc}")

def Fight():
	global ID
	enemytypes = ["light","heavy","boss"]
	cursor.execute("SELECT enemy_count, type FROM enemy WHERE type IN (SELECT enemy_id FROM locations WHERE game_id = %s) ", (ID,))
	enemyInfo = cursor.fetchall()[0]
	if enemyInfo[0] > 6:
		enemyInfo[0] -= random.randint(0, 3)
	choice = input("'go' to fight or 'leave' to leave").lower()
	while CheckInput(choice, ["go", "leave"]):
		choice = input("'go' to go or 'leave' to leave").lower()
	if enemyInfo[1] == "abandoned":
		TextColorIterate(["This airport is abandoned, you fix your plane and rest"], 10, 0.1, [Fore.YELLOW, Fore.WHITE], "loot.wav", False, "-", "\033[1m", "\033[0m")
		gameValues[2] += random.randint(20, 40) - int(gameValues[5]) * 5
		return
	elif enemyInfo[1] == "light":
		TextColorIterate(["This airport is guarded lightly"], 10, 0.1, [Fore.YELLOW, Fore.WHITE], "hurt.wav", False, "-", "\033[1m", "\033[0m")
		choice = input("'stay' to stay and fight, 'leave' to leave: ")
		while CheckInput(choice, ["stay", "leave"]):
			choice = input("'stay' to stay and fight, 'leave' to leave: ")
		if choice == "stay":
			gameValues[2] -= enemyInfo[0] * enemytypes.index(enemyInfo[1] + 1)
			checkHealth()
			gameValues[3] += 50 * enemyInfo[0] - int(gameValues[5]) * 3
		else:
			return
	elif enemyInfo[1] == "heavy":
		TextColorIterate(["This airport is guarded heavily"], 10, 0.1, [Fore.YELLOW, Fore.RED], "hurt.wav", False, "*", "\033[1m", "\033[0m")
		choice = input("'stay' to stay and fight, 'leave' to leave: ")
		while CheckInput(choice, ["stay", "leave"]):
			choice = input("'stay' to stay and fight, 'leave' to leave: ")
		if choice == "stay":
			gameValues[2] -= enemyInfo[0] * enemytypes.index(enemyInfo[1] + 1.5)
			checkHealth()
			gameValues[3] += 50 * enemyInfo[0] - int(gameValues[5]) * 3
		else:
			return
	elif enemyInfo[1] == "boss":
		TextColorIterate(["This airport has a boss"], 10, 0.1, [Fore.YELLOW, Fore.RED, Fore.BLACK], "boss.wav", False, "!", "\033[1m", "\033[0m")
		choice = input("'stay' to stay and fight, 'leave' to LEAVE: ")
		while CheckInput(choice, ["stay", "leave"]):
			choice = input("'stay' to stay and fight, 'leave' to leave: ")
		if choice == "stay":
			if gameValues[2] > 75:
				gameValues[2] -= 75
				gameValues[3] += 25000
				choice = input(f"You managed to beat your arch nemesis.\n'continue' to continue the game or 'quit' to quit the game: ")
				if choice == "continue":
					return
				elif choice == "quit":
					cmd_quit.action()
					return
			elif gameValues[2] <= 75:
				choice = input(f"Your arch nemesis shot you down.\n'new' to create a new game or 'quit' to quit the game: ")
				if choice == "new":
					deleteGame()
					cmd_new.action()
					return
				elif choice == "quit":
					cmd_quit.action()
					return
		else:
			return

		
def move():
	global ID
	global validCommands
	validCommands = [cmd_exit]
	inRange = getLocationsInRange()
	airportVals = []
	ICAOs = []
	print(ID)
	for vals in inRange:
		print(f"ICAO code: {vals[0]} \n" + f"Name: {vals[1]}\n" + f"Distance to: %.0f " % vals[2] + "km \n")
		ICAOs.append(vals[0].lower())

	choice = input("Input ICAO code of where you wanna move or exit: ").lower()
	cmdbool = False
	while True:
		if CheckCommands(choice):
			cmdbool = True
			break
		elif CheckInput(choice, ICAOs):
			break
		else:
			choice = input("Invalid input, Input ICAO code of where you want to move or 'exit' if you don't want to move: ").lower()
			pass
	if cmdbool:
		return
	else:
		for vals in inRange:
			if vals[0].lower() == choice:
				airportVals.extend(vals)
				break
		cursor.execute("UPDATE game SET gas = gas - %s, location = %s WHERE id = %s", (int(airportVals[2] / 3), airportVals[0], ID))
		cursor.execute("UPDATE location SET location = 1 WHERE airport_id =  %s", (airportVals[0], ))
		cnx.commit()
		checkHealth()
		Fight()
		
def doCommand(iput):
	for cmd in validCommands:
		if iput == cmd.name:
			cmd.action()
			return
	
q = lambda:TextColorIterate(["Bye!"], it = 50, wait = 0.02, c = [Fore.BLUE, Fore.GREEN, Fore.YELLOW], sound = "quit.wav", useClean = True, fillChar = " ", start = "\033[1m", end = "\033[0m")

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

TextColorIterate(s, 15, .075, useClean = True, sound = "intro.wav")
	
TextColorIterate(text = ["StartMenu"], c = [Fore.BLUE, Fore.YELLOW], fillChar = "-", it = 5, wait = .1, sound = "", start = "\033[1m", end = "\033[0m") 

validCommands = [cmd_new, cmd_load, cmd_quit]

choice = input("Input: make 'new' game, 'load' previous game or 'quit': ").lower()
while CheckCommands(choice):
	print("Input was insufficent")
	choice = input("Input: make 'new' game, 'load' previous game or 'quit': ").lower()
Clean()
startime = datetime.datetime.now()

while not choice == cmd_quit.name:
	validCommands = [cmd_help, cmd_quit, cmd_stats, cmd_move]
	cursor.execute("SELECT * FROM game WHERE id = %s", (ID,))
	gameValues = cursor.fetchall()[0]
	cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s", (gameValues[1],))
	gameLocation = cursor.fetchall()[0]
	if len(getLocationsInRange()) < 1:
		cursor.execute("UPDATE game SET gas = gas + 1000 WHERE id = %s", (ID,))
		cnx.commit()
		pass
	choice = input("What do you want to do? ").lower()
	while CheckCommands(choice):
		print("invalid input, input 'help' for commands")
		choice = input("What do you want to do? ").lower()
			
	
endtime = datetime.datetime.now() - startime
cursor.execute("UPDATE game SET time = ADDTIME(time,%s) WHERE id = %s", (endtime, ID))
cnx.commit()
cursor.close()
cnx.close()