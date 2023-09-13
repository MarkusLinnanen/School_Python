class Car:
	speed, traversed_distance = 0, 0
	def __init__(self, register, top_speed):
		self.register = register
		self.top_speed = top_speed
		
	def __str__(self):
		return f"register: {self.register}, top speed: {self.top_speed} km/h, speed: {self.speed} km/h, traversed distance: {self.traversed_distance} km"

car1 = Car("ABC-123", 143)

print(car1)