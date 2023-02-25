str1 = "luminar"
dict1 ={}
for index in range(1,len(str1)+1):
    dict1.setdefault(index,str1[index-1])
print(dict1)
# 2nd method
dict2 ={}
for i in range(1,len(str1)+1):
     dict2.update({})