""" Create an inner function to calculate the addition in the following way
•	Create an outer function that will accept two parameters, a and b
•	Create an inner function inside an outer function that will calculate the addition of a and b
•	At last, an outer function will add 5 into addition and return it"""
def my_fun(a,b):
    def addition(a,b):
        c = a+b
        return c
    res = addition(a,b)+5
    return res
a = int(input("enter first number"))
b = int(input("enter second number"))
print("the result is",my_fun(a,b))



