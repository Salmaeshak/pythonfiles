name = "salma"
for i in name:
    print(i)

for i in range(1,11):
    print(i)
# multiply a list of numbers
list = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in list:
    mult = i*n
    print(mult)

# sum of 1 t0 n numbers
n = int(input("enter the value of n "))
sum = 0
for x in range(0,n+1):
    sum = sum+x
print("sum of numbers is ",sum)

#print even numbers
for z in range(0,11,2):
    print(z)

#print odd numbers
for v in range(1,11,2):
    print(v)

#print the multiplication table of a given number
n2 = int(input("enter the value of n "))
for a in range (1,11):
    m = a*n2
    print(n2,"*",a ,"=",m)






