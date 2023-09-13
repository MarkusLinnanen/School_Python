import random

class Car:
	speed, traversed_distance = 0, 0
	def __init__(self, register, top_speed):
		self.register = register
		self.top_speed = top_speed

	def __str__(self):
		return f"register: {self.register}, top speed: {self.top_speed} km/h, speed: {self.speed} km/h, traversed distance: {self.traversed_distance} km"

	def accelerate(self, speed_change):
		self.speed += speed_change
		if(self.speed < 0):
			self.speed = 0
		elif(self.speed > self.top_speed):
			self.speed = self.top_speed
	
	def traverse(self, time):
		self.traversed_distance += self.speed * time

class Race:	
	# made the list of cars in init and took a number of cars as input
	# makes the class more modular and better in my opinion
	name, distance, cars = "", 0, []
	def __init__(self, n, d, c):
		self.name = n
		self.distance = d
		for i in range(c):
			self.cars.append(Car("ABC-" + str(i), random.randint(100, 200)))
							 
	def hourGoBy(self):
		for c in self.cars:
			c.accelerate(random.randint(-10,15))
			c.traverse(1)
							 
	def printSituation(self):
		for c in self.cars:
			print(c, "\n")
							 
	def raceOver(self):
		winner = Car("Not", 0)
		for c in self.cars:
			if c.traversed_distance > winner.traversed_distance:
				winner = c
			
		for c in self.cars:
			if c.traversed_distance >= self.distance:
				self.printSituation()
				print("Winner: " + winner.register)
				return True
			
		return False

rally = Race("Great Wreck Rally", 8000, 10)
hours = 0
while not rally.raceOver():
	rally.hourGoBy()
	hours += 1
	if not hours % 10:
		rally.printSituation()
	