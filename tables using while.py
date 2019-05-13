i=1
n=int(input("enter the number of tables needed starting from 1:"))
m=11    

while i<=n:
    j=1

    while j<m:
        print("%9d" %(i*j),end='')
        j+=1
    print()
    i+=1
