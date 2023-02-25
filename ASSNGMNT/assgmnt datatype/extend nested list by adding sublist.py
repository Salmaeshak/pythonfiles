list1 = ["a","b",["c",["d","e",["f","g"],"k"],"l"],"m","n"]
print(list1)
sublist = ["h","i","j"]
#for i in sublist:
list1[2][1][2].extend(sublist)
print(list1)
