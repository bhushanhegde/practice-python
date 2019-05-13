from math import pi

r=input("radius of the earthin million kilometers")
v=input("velocity of revolution in km")
r=float(r)
v=float(v)
r=r*1000000
year=2*pi*r/v
year=year/(60*60*24)
print(round(year))
