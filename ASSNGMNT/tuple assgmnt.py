#convert string to tuple
strn = "salma"
tpl = tuple(strn)
print(tpl)
#convert list to tuple
list1 = [1,2,3,4,"salma"]
tpl1 = tuple(list1)
print(tpl1)
#repeated items frm tuple
tpl2 = (23,4,5,4,6,5,7,8,8)
a = set()
for i in tpl2:
    if tpl2.count(i)>1:
        a.add(i)
print("the repeated items",a)

