a=input("enter the number:")
a=int(a)
i=0
while a>0:
    r=a%10
    a=a//10
    i=i*10+r
print(i)    
