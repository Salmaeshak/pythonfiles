# def test(a):
#     def add(b):
#         nonlocal a
#         a += 1
#         return a+b
#     return add
# func = test(4)
# print(func(8))
# 2nd method
def add(a,b):
    def add2(c):
        nonlocal a,b
        d = c+a+b
        return d
    return add2
fun = add(2,3)
print(fun(3))