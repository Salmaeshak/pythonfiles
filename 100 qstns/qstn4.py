"""Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')"""
l = []
n = int(input("enter the value of n: "))
for i in range(n):
   l.append(int(input("enter the number")))
print("the list is: ",l)
print("the tuple is: ",tuple(l))
