Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hegde="bhushan"
>>> hegde[2]
'u'
>>> hegde[2:6]
'usha'
>>> muddu="chaitali umesh bhagwat"
>>> muddu[0]
'c'
>>> muddu[3:9]
'itali '
>>> muddu[:9]
'chaitali '
>>> muddu[4:]
'tali umesh bhagwat'
>>> muddu[]
SyntaxError: invalid syntax
>>> muddu[:]
'chaitali umesh bhagwat'
>>> muddu[-1]
't'
>>> muddu[-1:1]
''
>>> muddu[1:-1]
'haitali umesh bhagwa'
>>> muddu[1:0]
''
>>> muddu[9:5]
''
>>> muddu[10:16]
'mesh b'
>>> muddu[10:100]
'mesh bhagwat'
>>> muddu[8*9]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    muddu[8*9]
IndexError: string index out of range
>>> len("qwertyuiopasdfghjklzxcvbnm")
26
>>> u="wertyuidfghjk"
>>> len(u)
13
>>> 
