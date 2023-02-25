employee = {"name":"salma","age":28,"salary":35000}
print(employee)
print(employee["name"])
print(employee["age"])
g = employee.get("name")
print(g)
k = employee.keys()
print(k)
v = employee.values()
print(v)
i = employee.items()
print(i)
employee["salary"] = 50000
print(employee)
employee.update({"age":30})
print(employee)
employee.update({"name":"amina","age":2})
print(employee)
employee["colour"] = "white"
print(employee)
employee.update({"sex":"f"})
print(employee)
employee.pop("colour")
print(employee)
employee.popitem()
print(employee)
del employee["name"]
print(employee)
dict1 = {"name":"salma","age":28,"salary":28000}
del employee
dict2 = {"car":"tata","model":2016}
dict2.clear()
print(dict2)
