n = int(input("enter the number:"))
f = 0
# n=5 ... 5%1=0 5%2=1 5%3=2 5%4=3 5%5=0
if n==1:
    print("not defined")
else:
    for i in range(1,n+1):
       if n%i == 0:
        f = f+1
    if f==2:
        print("the number is prime")
    else:
        print("the number is not prime")

