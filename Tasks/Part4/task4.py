import random
print("Welcome to the quessing game, a game where you try to quess the number")
num = random.randint(1, 10)
i = True
while i:
	inp = int(input("Input number between 1 and 10: "))
	if inp == num:
		print("Congrats! you guessed the number")
		i = False
	else:
		print("Quess again")