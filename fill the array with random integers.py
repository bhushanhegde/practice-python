from random import randint

def l(a,q,mi,ma):
    for i in range(q):
        a.append(randint(mi,ma))





m=int (input("enter the minimum term:"))
n=int (input("enter the max term:"))
z=int (input("enter the quantity:"))
a=[ ]

l(a,z,m,n)
print(a)       
