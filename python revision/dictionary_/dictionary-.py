#add an element
dict1 = {"name":"salma","age":30}
dict2 = {"adrs":"abc"}
dict1.update(dict2)
print(dict1)
dict1.update({"course":"python"})
print(dict1)
# add elements in an empty dict
d ={}
n = int(input("enter the number of elements in dictionary:"))
for i in range(n):
    key = int(input("enter the key:"))
    value = input("enter the value:")
    d.update({key:value})
print(d)

#key,value,items
for i in d.values():
    print(i)
for i in d.keys():
    print(i)
for i,j in d.items():
    print(i,j)

#get method
x = d.get(2)
print(x)