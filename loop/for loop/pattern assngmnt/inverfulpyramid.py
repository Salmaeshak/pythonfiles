#inverted full pyramid
n = int(input("enter the value of n: "))
for i in range(0,n+1):
    for s in range(i):
        print(" ",end="")
    for j in range(n-i):
        print(" *",end="")
    print()
