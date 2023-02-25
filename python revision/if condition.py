# #check wether the number is positive or negative or zero
# a = int(input("enter a number"))
# if a>0:
#     print("the given number is positive")
# elif a<0:
#     print("the given number is negative")
# else:
#     print("the number is zero")
#
#check the greatest number using nested if
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
c = int(input("enter the third number:"))
if a>b:
    if a>c:
        print(a,"is greater")
    else:
        print(c,"is greater")
elif b>c:
    print(b,"is greater")
else:
    print(c,"is gtreter")
