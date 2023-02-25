# factorial of a number
def fact(num):
    result = 1
    for i in range(1,num+1):
        result = result*i
    return result
num1 =int(input("enter a number:"))
print("the factorial of the number {} is {}".format(num1,fact(num1)))
