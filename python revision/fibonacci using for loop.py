n = int(input("enter the number of terms :"))
a,b = 0,1
print("fibonacci series:")
print(a)
print(b)
for i in range(3,n+1):
    c=a+b
    print(c)
    a,b = b,c

