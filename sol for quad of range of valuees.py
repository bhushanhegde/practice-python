import math

a1=int(input("enter the range of a:"))
a2=int(input())
b1=int(input("enter the range of b:"))
b2=int(input())
c1=int(input("enter the range of c:"))
c2=int(input())

a=range(a1,a2+ 1)
b=range(b1,b2+1)
c=range(c1,c2+1)

for i in a:
    if i==0:
        continue
    for j in b:
        for k in c:
            print(i,j,k,end='')
            D=j*j-4*i*k
            if D>=0:
                x1=(-j+math.sqrt(D))/(2*i)
                x2=(-j-math.sqrt(D))/(2*i)
                x1=round(x1,2)
                x2=round(x2,2)
                print("the roots are:",x1,x2)
            else:
                    print("thre is no root")
#i like this program!!!
