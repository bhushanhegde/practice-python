import math

n=int (input())

if n<2:
    print("enter big number bro....1 is prime ..")
    quit()
elif n==2:
    print("the number is prime only")
    quit()
i=2

a=int(math.sqrt(n))

while i<=a:
    if n%i==0:
        print("the given number is composit")
        quit()
    i+=1

print("the given number is prime")    


    
