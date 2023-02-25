#search()
import re
str = 'class will start at 10am'
a = re.search('\s',str)
print(a)
print(a.start())#start() returns the start position
d = re.search('\d',str)
print(d.start())
s = re.search('python',str)
print(s)

m = re.search('^class.*10am$',str)
if m:
    print('found')
else:
    print('not found')