#reverse pyramid with number
n = int(input("enter the value of n:"))
for i in range(n):
    for j in range(n-i,0,-1):
        print(j,end="")
    print()