str = 'cat rat mat cat pat rat cat sat cat sat'
list1 = str.split(' ')
d = {}
for i in list1:
    if i in d:
        d[i] =d[i]+1
    else:
        d[i] = 1
print(d)