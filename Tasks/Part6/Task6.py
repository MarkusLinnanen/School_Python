import math

def CalculatePrice(diameter, price):
	area = math.pi/4 * diameter**2
	return price / diameter

p1dia = float(input("Input pizza diameter: "))
p1pri = float(input("Input pizza price: "))
p2dia = float(input("Input second pizza diameter: "))
p2pri = float(input("Input second pizza price: "))

if CalculatePrice(p1dia, p1pri) <= CalculatePrice(p2dia, p2pri):
	print("First pizza was better value for money")
else:
	print("Second pizza was better value for money")