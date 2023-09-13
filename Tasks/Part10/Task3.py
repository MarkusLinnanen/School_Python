class elevator:
	floor = 0
	def __init__(self, bottom, top):
		self.bottom = bottom
		self.floor = bottom
		self.top = top
	
	def goup(self):
		self.floor += 1
		   
	def godown(self):
		self.floor -= 1
	
	def gotofloor(self, f):
		while not (f == self.floor):
			if f > self.floor:
				self.goup()
				
			elif f < self.floor:
				self.godown()				
				
class house:
	elevators = []
	botfloor, elevamount = 0, 0
	def __init__(self, bot, top, eamount):
		self.botfloor = bot
		self.elevamount = eamount
		for i in range(self.elevamount):
			self.elevators.append(elevator(bot, top))
		print(self.elevators[eamount - 1].floor)
			
	def driveElevator(self, elevnum, floor):
		e = self.elevators[elevnum % self.elevamount]
		e.gotofloor(floor)
		print(f"Elevator {elevnum % self.elevamount} is now on floor: {e.floor}")
	
	def fireAlarm(self):
		for e in self.elevators:
			e.gotofloor(self.botfloor)
		
	def __str__(self):
		s = "Elevator floors: "
		for e in self.elevators:
			s += str(e.floor) + " "
		return s
		
h = house(-2, 10, 6)
h.driveElevator(11, 7)
print(h)
h.fireAlarm()
print(h)