listofdict = [{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},{"V":"S009"},{"VIII":"S007"}]
setofvalues = set() #set not allow duplicate elements
for i in listofdict:
    for value in i.values():
        setofvalues.add(value)
print(setofvalues)
#second method

ul =[]
for i in listofdict:
    ul.extend(list(i.values()))
ul =set(ul)
print(ul)