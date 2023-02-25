dict1 = {1:2,3:4,4:3,2:1,0:0}
print("the dictionary is: ",dict1)
val =list(dict1.items()) #list of tuple of key value pair
newval = []
newvalf = []
for i in val:
    irev = i[::-1]
    newval.append(irev) #value key pair in newval
val.clear()
newval.sort() #sort value key pair
#print(newval)
for i in newval: #setting back to key value pair
    irevef = i[::-1]
    val.append(irevef) #append sorted key value pair in val
#print(val)
newvalf = val[::-1] #reverse val for getting descending order
#print(newvalf)
print("dictionary in ascending order",dict(val))
print("dictionary in descending order",dict(newvalf))





