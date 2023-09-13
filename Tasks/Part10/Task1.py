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
			
e = elevator(-1, 10)
e.gotofloor(6)
e.gotofloor(-1)