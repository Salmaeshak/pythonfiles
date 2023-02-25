# add a list of elemnts to a set
set1 = {1,2,3,4,5,6}
list1 = [2,56,7,8]
set1.update(list1)
print(set1)

# get only unique items from two sets
a = {1,2,3,4,5,7}
b = {1,2,8,9,3}
print("the sets are",a,b)
print("the unique items are",a|b)

#check if any elemnets in set is common , if yes, display the common elemnt
c = {1,2,3,4,5,7,6}
d = {5,6,7,8,9,10}
if c.isdisjoint(d):
    print("there is no common elements are")
else:
    print("the common elements are",c&d)

# remove items from set1 that are not common to set1 and set2
set1 ={1,4,3,8,56,7,2}
set2 ={1,5,9,0,10,3,2}
print("the sets are",set1,set2)
print("the set after removing the elements is",set1.intersection_update(set2))