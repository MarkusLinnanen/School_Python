import random

diceamount = int(input("Input the amount of dice to be thrown: "))
total = 0
i = 0
dice = []
while i < diceamount:
	dice.append(random.randint(1, 6))
	i += 1
	
for x in dice:
	total += dice[x]
	
print(total)