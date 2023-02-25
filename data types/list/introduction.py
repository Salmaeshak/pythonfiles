lis1= [1,2,34,4]
print(lis1)
print(lis1[1])
print(lis1[2])
#nested list
my_list = ["salma",[1,5,7],"amina"]
print(my_list)
print(my_list[1])
print(my_list[1][1])
print(my_list[-1])
print(my_list[-2])

#append
list1 = [2,4,3,2]
list1.append(3)
print(list1)

#remove
list2 = [2,4,6,2,3]
list2.remove(3)
print(list2)

#extend
list2.extend(list1)
print(list2)

#insert
list3 = ["asb",1,2,3,4]
list3.insert(2,"salma")
print(list3)
list6 = ["salma",[1,2,3,4]]
list6[1].insert(3,4)
print("list6 is",list6)


#count
print(list2.count(2))

#reverse
list4 =['join',2,3,4,6,7,1]
list4.reverse()
print(list4)

#sort
list5 = [6,4,3,8,9,1,2,3,4]
list5.sort()
print(list5)

#pop
list7 = [2,3,4,5,6]
list7.pop(2)
print("list7 is ",list7)

#index
print(list7.index(6))

#copy
list11 = ["salma",1,2,3,4,9]
list11.copy()
print("copy of list11 is ",list11)
#clear
list12 = [1,2,3,4]
list12.clear()
print(list12)











