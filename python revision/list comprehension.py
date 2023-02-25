l = [x+2 for x in [1,2,3]]
print(l)
# all even numbers under 25
l1 = [x for x in range(0,25) if x%2==0]
print(l1)
#get all vowels from string
v = [i for i in "hello world" if i in ['a','e','i','o','u']]
print(v)
#get first letter of all the words in a sentence
str = "hai hello salma"
ls = str.split(" ")
print(ls)
lst = [i[0] for i in ls ]
print(lst)

#return the words where e is present
colours = ['red','white','green','pink']
lsc = [i for i in colours if 'e' in i]
print(lsc)

#return words not green
lsc1 = [i for i in colours if i!='green']
print(lsc1)

#converts all words in to uppercase
lsu = [i.upper() for i in colours]
print(lsu)

#
lse = [i if i!='green'else 'blue' for i in colours]
print(lse)