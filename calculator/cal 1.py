#calculator
operator = input("+ for addition,- for substraction,* for multiplication,/ for division = ")

number1 = int(input("enter the first number = "))
number2 = int(input("enter the second number = "))

if operator == '+': print("sum is " ,number1+number2)
elif operator == '-': print("difference is ",number1-number2)
elif operator == '*': print("multiplication is ",number1*number2)
elif operator == '/': print("division is ",number1/number2)
else :print("invalid")

