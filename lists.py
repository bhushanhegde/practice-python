Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> fib=[0,1,1,2,3,5,8,13]
>>> print(fib)
[0, 1, 1, 2, 3, 5, 8, 13]
>>> fib[2]
1
>>> fib[10]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    fib[10]
IndexError: list index out of range
>>> fib[6]=45
>>> fib
[0, 1, 1, 2, 3, 5, 45, 13]
>>> fib
[0, 1, 1, 2, 3, 5, 45, 13]
>>> fib[100]=34
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    fib[100]=34
IndexError: list assignment index out of range
>>> fib+[12,13]
[0, 1, 1, 2, 3, 5, 45, 13, 12, 13]
>>> fib
[0, 1, 1, 2, 3, 5, 45, 13]
>>> fib.append(12,13)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    fib.append(12,13)
TypeError: append() takes exactly one argument (2 given)
>>> fib.append(13)
>>> fib
[0, 1, 1, 2, 3, 5, 45, 13, 13]
>>> [0, 1, 1, 2, 3, 5, 45, 13, 13]
[0, 1, 1, 2, 3, 5, 45, 13, 13]
>>> 
>>> 
>>> fib[:3]
[0, 1, 1]
>>> fib[:3]=[0,0,0]
>>> fib
[0, 0, 0, 2, 3, 5, 45, 13, 13]
>>> fib
[0, 0, 0, 2, 3, 5, 45, 13, 13]
>>> fib[:]=[]
>>> 
>>> fib
[]
>>> fib[:2]
[]
>>> fib[:5]=[1,2,3,4,5]
>>> fib
[1, 2, 3, 4, 5]
>>> 
