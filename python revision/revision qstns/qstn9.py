"""WAP to print intiger value in list using list comprehension"""
ls = [12,66,12.45,34,45.34,42]
result = [x for x in ls if type(x)==int]
print(result)
