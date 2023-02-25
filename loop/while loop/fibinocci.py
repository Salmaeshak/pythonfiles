#fibonacci series
n = int(input("enter the value of n :"))
n1 = 0
n2 = 1
sum = 0
while(n1<=n):
    sum=n1+n2
    print(n1,end=' ')
    n1=n2
    n2=sum
