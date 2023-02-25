def upper_decor(fun):
    def inner():
        result = fun()
        return result.upper()
    return inner()
def my_string():
    return "hello"
f = upper_decor(my_string)
print(f)

#with symbol
def upper_decor(fun):
    def inner():
        result = fun()
        return result.upper()
    return inner()
@upper_decor #print(upper_decor(my_string))
def my_string():
    return "hello"