#lambda function is an anonymous function
x = lambda a : a+10
print(x(3))

y = lambda a,b : a*b
print(y(2,3))
#lambda function in another function
def my_fun(n):
    c = lambda a : a*n
    return c
func = my_fun(3)
print(func(4))

