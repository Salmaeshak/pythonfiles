#qstn 1 half pyramid of numbers

row = int(input("enter the number of rows "))
for i in range(0,row+1):
    for j in range(i):
        print(j+1,end=" ")
    print()

#qstn revers pyramid
row1= int(input("enter the number of rows "))
for i in range(row1):
     for j in range(row1-i,0,-1):
         print(j,end=" ")
     print()
#qstn 3 full pyramid
n = int(input("number of rows"))
for i in range(n):
    for s in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()



