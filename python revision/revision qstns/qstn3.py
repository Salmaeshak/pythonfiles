"""check two list have common elements"""
l1 = [3,2,5,7,8,9,1]
l2 = [21,3,4,6,5,7]
l3 = []
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i] == l2[j]:
            l3.append(l1[i])
if len(l3)==0:
    print("no common elements found")
else:
    print("the common elements are:",l3)