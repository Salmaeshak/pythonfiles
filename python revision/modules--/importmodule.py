import my_modules
while True:
    opt = int(input("1 create\n 2 search\n 3 remove\n 4 replace \n enter the choice:"))
    if opt ==1:
       my_modules.create()
    elif opt ==2:
        my_modules.search()
    elif opt == 3:
        my_modules.remove()
    elif opt == 4:
        my_modules.replace()
    else:
        break



