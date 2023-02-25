f = open('test2','r')
d = {}
for i in f :
    var = i.split(" ")
    for j in var:
        if j in d:
            d[j] = d[j]+1
        else:
            d[j] = 1
print(d)
