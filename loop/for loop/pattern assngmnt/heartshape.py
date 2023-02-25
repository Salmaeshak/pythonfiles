n = int(input("enter the value of n "))
half = n//2
for i in range(2,half):
    print(" "*(half-i-1)+"*"*(2*i+1)+"  "*(half-i)+"*"*(2*i+1))
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))
