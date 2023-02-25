n = int (input("enter the number"))
rev = 0
p =1
s = 0
while n!=0:
    num = n%10
    rev = rev*10+num
    p = p*num
    s = s+num
    n = n//10
print("the reverse of the number is:",rev)
print("the product of the number is :",p)
print("the sum of the number",s)



