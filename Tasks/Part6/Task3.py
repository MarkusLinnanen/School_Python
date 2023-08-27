def GallonToLitre(gallons):
		return gallons * 3.785

i = 1
while i >= 0:
	i = float(input("Enter gallons to make litres: "))
	if i >= 0:
		print("%.2f" % GallonToLitre(i))