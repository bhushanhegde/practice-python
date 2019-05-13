t=input()
sign = t[-1]
t=int(t[:-1])
if sign=='c' or sign=='C':
    t=round(t*(9/5)+32)
    print(str(t)+'F')
elif sign=='f' or sign=='F':
    t=round((t-32)*(5/9))
    print(str(t)+'c')
    
