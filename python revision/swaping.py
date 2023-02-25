a,b = 10,20
t = a
a =b
b = a

#2nd method
a = a+b
b = a-b
a = a-b

#python method
c,d = int(input("enter a number:")),int(input("enter a number:"))
c,d = d,c
print("a=",c)
print("b=",d)