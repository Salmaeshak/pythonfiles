#split()
import re
str = 'class will start at 10am'
s = re.split(' ',str)
print(s)

s1 = re.split('a',str)
print(s1)

s2 = re.split(' ',str,2)
print(s2)