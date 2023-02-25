prime = [x for x in range(2,21) if all(x%y!=0 for y in range (1,x))]
print(prime)