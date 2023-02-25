n = 6
num = 65
for i in range(0,n):
    for j in range(0,i+1):
        alp = chr(num)
        print(alp,end="")
        num = num+1
    print()
    