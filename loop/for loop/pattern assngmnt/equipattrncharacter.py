n = 6
num = 65
for i in range(n):
    for s in range(n-i):
        print(" ",end="")
    for j in range(i+1):
        alp = chr(num)
        print(alp," ",end="")
        num = num+1
    print()

