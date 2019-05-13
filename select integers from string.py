s=input()
l=len(s)
i=0
while i<l:
     num=''
     symbol=s[i]

     while symbol.isdigit():
         num+=symbol
         print(num)
         i+=1   
