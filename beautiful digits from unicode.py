digits = {0:9471, 1:10102,2:10103,
          4:10104,5:10105,5:10106,
          6:10107,7:10108,8:10109,
          9:10110,10:10111}

n=input("input:")

new_n=""

for i in n:
    q=int(i)
    i=chr(digits[q])
    new_n=new_n+i
print("the output is:%s"%new_n)
    
