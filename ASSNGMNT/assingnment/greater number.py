a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print("the greater number is",a)
elif b>a and b>c:
    print("the greater number is",b)
elif c>a and c>b:
    print("the greater number is",c)
else:
    print("invalid number")