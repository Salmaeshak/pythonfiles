#sub()
import re
input = 'rose and jasmine are flowers'
s = re.sub(' ','*',input)
print(s)
r = re.sub(' ','*',input,3)
print(r)