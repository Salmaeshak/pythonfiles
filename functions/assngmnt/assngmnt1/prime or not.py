#prime or not
def prime(num):
    flag = 0
    half = num//2
    for i in range(2,half+1):
        if(num%i)==0:
                flag = 1
                break
    if flag ==0:
        print("the number is prime")
    else:
        print("the number is not a prime")
num1 = int(input("enter a number"))
prime(num1)