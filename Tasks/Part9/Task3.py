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

car1 = Car("ABC-123", 143)

car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(car1.speed)

car1.accelerate(-200)
print(car1.speed)