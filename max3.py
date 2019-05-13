b=int(input())
a=int(input())
c=int(input())
#print("the integers are"+a,b,c)
if b>=a & b>=c:
    print(" larger number is ",b)
elif a>=b & a>=c:
    print(" larger is ",a)
else:
    print(" larger",c)
