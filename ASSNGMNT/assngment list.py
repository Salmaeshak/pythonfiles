#qstn 1 sum of element
my_list = [1,2,3,4,5]
total= 0
for n in range(0,len(my_list)):
    total = total+my_list[n]
print("sum of all elements in list ",total)

#qstn 2 largest number
list = [1,2,-8,0]
largest = 0
for n in range(0,len(list)):
    if list[n]>largest:
       largest = list[n]
print(largest)

#qstn 3 list to string
s = ['p','y','t','h','o','n']
l = type(str(s))
print(l)

#qstn 4 multiply the element
list1 = []
n = int(input("enter the number of element in list = "))
for x in range(0,n):
    ele = int(input("enter the element "))
    list1.append(ele)
print("the list is ",list1)
multiply=1
for i in range(0,n):
    multiply = multiply * list1[i]
print("the product of the elements in list",multiply)







