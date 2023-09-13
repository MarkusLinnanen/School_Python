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
				
			print(self.floor)
				
class house:
	elevators = []
	def __init__(self, bottom, top, elevamount):
		for i in range(elevamount):
			self.elevators.append(elevator(bottom, top))
			
	def driveElevator(self, elevnum, floor):
		self.elevators[elevnum - 1].gotofloor(floor)
			
h = house(-2, 10, 5)
h.driveElevator(5, 7)