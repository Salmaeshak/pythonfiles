"""WAP to extract numbers from a string using list comprehension"""
strn = 'the room number 45 and 67 are vaccant'
ls = [x for x in strn if x.isdigit()]
print(ls)