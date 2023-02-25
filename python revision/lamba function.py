add = lambda a,b : a+b
print(add(2,3))
#syntax - lambda arguments : expression

#largest
large = lambda a,b : a if a>b else b
print(large(4,56))

#filter,map ,reduce
l = [2,4,5,6,7]
ls = list(filter(lambda x : x%2==0 ,l))
print(ls)

l1 = [2,4,3,1]
ls1 = list(map(lambda a : a*2 ,l1))
print(ls1)

l2 = [1,2,3,4]
from functools import reduce
product = reduce(lambda x,y : x*y ,l2)
print(product)
