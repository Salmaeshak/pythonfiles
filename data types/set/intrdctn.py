
"""
* Immutable
* unorderd
* duplicates are not allowed
* unindexed
* set items are immutable , bt remove items and add items
"""
set1 ={1,2,"salma"}
print(set1)
 #set not allow list(mutable data types)
set2 = set([1,2,3,4])
print(set2)

#mathematical operations
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}
print(a|b) #union
print(a&b) #intersection
print(a-b) #difference
print(a^b) # symmetric difference