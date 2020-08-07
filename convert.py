#This program will help to convert special char in git username and password in % format.

import sys
var1 = sys.argv[1]

list_of_char = {'!' : '%21'  , '#' : '%23' ,  '$'  : '%24' ,  '&' : '%26' ,  "'" : '%27' ,  '(' : '%28' ,  ')' : '%29' ,  '*' : '%2A'  , '+' : '%2B' ,  ',' : '%2C' ,  '/' : '%2F' ,  ':' : '%3A' ,  ';' : '%3B' ,  '=' : '%3D' ,  '?' : '%3F'  , '@' : '%40'  , '[' : '%5B'  , ']' : '%5D'}

for k in list_of_char:
    for i in var1:
        if k == i:
            var1=var1.replace(i,list_of_char[i])
print(var1)
