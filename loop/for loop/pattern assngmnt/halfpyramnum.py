#half pyramid with number
n = int(input("enter the value of n: "))
for i in range(1,n+1):
    for j in range(i):
        print(j+1,end="")
    print()
