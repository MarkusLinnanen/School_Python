i = int(input("Input month number: "))
timeofyear = ("Winter", "Spring", "Summer", "Fall")
monthofyear = (12, 1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10, 11)
print(timeofyear[monthofyear.index(i) // 3])