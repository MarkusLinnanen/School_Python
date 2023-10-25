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
        if (self.speed < 0):
            self.speed = 0
        elif (self.speed > self.top_speed):
            self.speed = self.top_speed

    def traverse(self, time):
        self.traversed_distance += self.speed * time


class Electric(Car):
    def __init__(self, register, top_speed, batterysize):
        super().__init__(register, top_speed)
        self.batterysize = batterysize
    def __str__(self):
        return f"register: {self.register}, top speed: {self.top_speed} km/h, speed: {self.speed} km/h, traversed distance: {self.traversed_distance} km, {self.batterysize} kWh in batterysize"



class Gas(Car):
    def __init__(self, register, top_speed, tanksize):
        super().__init__(register, top_speed)
        self.tanksize = tanksize


gc = Gas("ABC-15", 180, 52.5)
ec = Electric("ABD-123", 165, 32.3)
gc.speed = 50
ec.speed = 45
ec.traverse(3)
gc.traverse(3)

# didn't know what was the tasks meaning so one is original __str__ the other one is redone
print(ec)
print(gc)
