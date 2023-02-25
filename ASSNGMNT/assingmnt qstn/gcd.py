n1 = int(input("enter a number: "))
n2 = int(input("enter a number :"))
if n1>n2:
    small = n2
else:
    small = n1
for i in range(1,small+1):
    if((n1%i==0) and (n2%i==0)):
        gcd = i
print("gcd of %d and %d is %d"%(n1,n2,gcd))
