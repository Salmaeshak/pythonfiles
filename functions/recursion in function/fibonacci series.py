def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

n = int(input("enter the number of terms:"))
for i in range(n):
    print(fibo(i))
