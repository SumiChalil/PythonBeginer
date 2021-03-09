import math
## To find the area and circumference of a cicle
r = int(input ("Enter the radiaus of the circle "))
pi = math.pi
area = pi * (r ** 2)
circum = 2 * pi * r
print("Area = " , round(area,2))
print('Circumference =' , round(circum,2))

