#pass a range() fuction to a list constructor to create a list
def evn_list(a,b):
    e = []
    for i in range(a,b,2):
        e.append(i)
    return e
start = int(input("enter the starting number"))
end = int(input("enter the ending number"))
print(evn_list(start,end))