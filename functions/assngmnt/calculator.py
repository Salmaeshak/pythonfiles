def sum1(a,b):
    c = a+b
    return c
def diff(a,b):
    c = a-b
    return c
def mul(a,b):
    c = a*b
    return c
def div(a,b):
    c = a/b
    return c
num1 = int(input("enter the first number"))
num2 = int(input("enter the second number"))
oper =input("enter + for addition\n\t - for substraction \n\t * for multiplication \n\t / for division")
if oper == "+":
    print("the sum of the numbers are",sum1(num1,num2))
elif oper == "-":
    print("the differents of the numbers are",diff(num1,num2))
elif oper == "*":
    print("the product of the numbers are",mul(num1,num2))
elif oper == "/":
    print("division of the two numbers are",div(num1,num2))
else:
    print("enter a valid operation")
