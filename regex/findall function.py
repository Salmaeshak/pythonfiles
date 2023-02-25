#findall()
import re
str1 = 'rose is a beautiful and colourful flower'
s = re.findall('ful',str1)
print(s)
s1 = re.findall('full',str1)
print(s1)
#[scr]
d = 'cat mat rat pat sat'
a = re.findall('[scr]at',d)
print(a)
#[^scr]
d1 = 'cat mat rat pat sat'
a1 = re.findall('[^scr]',d)
print(a1)
#\d{3}
d2 = 'cat mat rat pat sat 99988 999'
a2 = re.findall('\d{3}',d2)
print(a2)
#\d{1,3}
d3 = 'cat mat 99988 9999 6666'
a3 = re.findall('\d{1,3}',d3)
print(a3)
#\b\d{4}\b
a4 = re.findall(r'\b\d{4}\b',d3)
print(a4)
