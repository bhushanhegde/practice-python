a=input()
a=int(a)

f1=f2=1

print(f1,f2)

i=2
while i<a:
    f1,f2=f2,f1+f2
    print(f2)
    i+=1

