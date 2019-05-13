from random import randint

k=randint(1,10)

a=0

c=1

while k!=a:
    print("%2d try:"%c,end='')
    a=int(input())
    if a>k:
        print("u r very high")
    elif a<k:
        print("u r very low")
    else:
        print("u guessed it!!!!")
        quit()
    c+=1
    if c>3:
        print("u r the programer")
        
        quit()
