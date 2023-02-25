"""WAP to print all numbers in range divisible by a given number"""
lower = int(input('enter the lower limit:'))
upper = int(input('enter the upper limit:'))
n = int(input('enter the number:'))
for i in range(lower,upper+1):
    if (i%n==0):
        print(i)