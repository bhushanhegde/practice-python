from math import pi

h=float(input('enter the hight:'))

r=float(input('enter the radius:'))

circles=2*(pi*r**2)

side=pi*r*h*2

area=circles+side

print("the area of the cylinder is ",round(area))
