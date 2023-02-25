#access 20 frm tuple
tpl = (1,2,40,30,20)
ls = list(tpl)
ls[4] = 100
print(tuple(ls))
# access 20 frm nested tuple
tpl1 = (1,2,40,(10,2,30),[30,20,10],40)
print(tpl1)
ls1 = list(tpl1)
ls1[4][1] = 100
print(tuple(ls1))
#to remove repeated elemnt frm tuple
tpl2 = (1,2,40,40)
print("the original tuple is",tpl2)
re = tuple(set(tpl2))
print("the tuple after removing the repeated elements",re)


