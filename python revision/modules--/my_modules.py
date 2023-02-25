l= []
def create():
    n = int(input("enter the numbers of elements in list:"))
    for i in range(0,n):
        temp = int(input("enter the element:"))
        l.append(temp)
    print("the list is:",l)

#create()
#search the items in the list
def search():
    item = int(input("enter the element:"))
    if item in l:
        print("found the item")
    else:
        print("not found")
# search()
#remove items from list
def remove():
    item = int(input("enter the element to be removed:"))
    if item in l:
       l.remove(item)
       print("the list after removing the element:",l)
    else:
        print("the item is not found in list")
# remove()
#replace an element
def replace():
    relemnt = int(input("enter the element to be repleced:"))
    nelemnt = int(input("enter the elemnt to be added:"))
    for i in range(len(l)):
        if l[i] == relemnt:
           l[i] = nelemnt
        else:
            print("the elemnt is not found to be replace")
    print("the new list is:",l)
#replace()
while True:
    opt = int(input("1 create\n 2 search\n 3 remove\n 4 replace \n enter the choice:"))
    if opt ==1:
        create()
    elif opt ==2:
        search()
    elif opt == 3:
        remove()
    elif opt == 4:
        replace()
    else:
        break

