# tple = (1,2,34,"salma",(2,3,4))
# print(tple)
# print(type(tple))
# print(len(tple))
# print(tple[0])     #indexing
# print(tple[-1])    #negative indxng
# print(tple[2:4])   #slicing
# print(tple[::-1])   #reversing
# print(tple[-4:-1])   #negative slicing
#
# # to update a tuple
# ls = list(tple)
# ls[0] = "amina"
# tple = tuple(ls)
# print(tple)
#
# #to append a tuple
# l = list(tple)
# l.append("eshak")
# tple = tuple(l)
# print(tple)
#
# #append a tuple in to a tuple
# tpl2 = ("ardeshir",5,"m")
# tple += tpl2
# print(tple)
#
# #remove
# y = list(tple)
# y.remove("eshak")
# tple = tuple(y)
# print(tple)
#
# #delete
# tp = (1,3,5,6,7,8)
# del tp
#
#
# # while loop
# tl = ("apple","orange","banana")
# i=0
# while i<len(tl):
#     print(tl[i])
#     i+=1
#
# #unpacking
# fruits = ("apple","orange","pappaya","mango","cherry")
# (green,*tropic,red) = fruits
# print(green)
# print(*tropic)
# print(red)
# #nested tuple
#
# emp = ("salma",[1,2,3],"age",28,3,3,3)
# print(emp[0])
# print(emp[1][1])
# emp[1][2]= "amina"
# print(emp)
#
# print(emp.index(28)) #index
# print(emp.count(3)) #count
#
# print("salma" in emp)

#tuple methods
tpl = (1,2,3,4,5,98,0)
print(len(tpl))
print(max(tpl))
print(min(tpl))
print(sorted(tpl))
print(sum(tpl))
print(all(tpl))
print(any(tpl))
#enumerate
y = enumerate(tpl)
print(tuple(y))

name = ["salma","simi","siyan"]
age = [30,25,16]
for i,(name,age) in enumerate(zip(name,age)):
    print(i,name,age)

alp = [('a','b'),('c','d')]
y = enumerate(alp)
print(tuple(y))

for i,alp in enumerate(alp):
    print(i,alp)
#map() can listify the list of string individualy
l = ['salma','simi']
t = list(map(tuple,l))
print(t)
s = tuple(map(list,l))
print(s)
se = set(map(set,l))#set can't map
print(se)







