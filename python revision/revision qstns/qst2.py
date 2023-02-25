"""pyramid of horizontal number table"""
row = int(input("enter the number of rows:"))
for i in range(1,row+1): #for row
    for j in range(1,i+1): #for column
        print(i*j,end=" ")
    print()