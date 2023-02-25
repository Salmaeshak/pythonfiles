number = int(input(" enter a number : "))
#n = len(str(number))
sum = 0
num = number
while(num!=0):
    digit = num%10
    sum = sum + digit**3
    num = num//10
if number==sum:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")