import random

#Made shure that the input goes well
def FourDigitCode(r, minnum, maxnum):
	s = ""
	for i in range(r):
		s += str(random.randint(abs(int(minnum % 10)), abs(int(maxnum % 10))))
		
	print(s)
	
random.seed(random.randint(0, 100000))

FourDigitCode(3, 0, 9)
FourDigitCode(4, 1, 6)