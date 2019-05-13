import math

r=input("radius of the orbit(in million kilometers )")
v=input("orbital speed(km/se):")
r=float(r)
v=float(v)

r=r*1000000

year=2* math.pi*r/v

year=year/(60*60*24)

print(round(year))
