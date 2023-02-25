dict1 = {1:{"name":"salma","age":30,},2:{"salary":38000,"sex":"f"}}
print(dict1)
print(dict1[1]["name"])
dict1[3] = {"car":"toyota","model":2014}
print(dict1)
x = dict1.values()
print(x)
print(dict1.keys())
g = dict1.get(1)
print(g)
print(dict1.pop(2))
print(dict1.items())
dict1.update({4:{"adrss":"abc","place":"def"}})
print(dict1)
del dict1[1]
print(dict1)
dict2 = dict1.copy()
print(dict2)
dict1.clear()
print(dict1)


