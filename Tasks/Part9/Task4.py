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
	
cars = []
for i in range(10):
	cars.append(Car("ABC-" + str(i), random.randint(100, 200)))

b = True
while b:
	for i in range(10):
		cars[i].accelerate(random.randint(-10,15))
		cars[i].traverse(1)
		if(cars[i].traversed_distance >= 10000):
			print("winner: " + cars[i].register)
			b = False
			break
		print(cars[i], "\n")
	