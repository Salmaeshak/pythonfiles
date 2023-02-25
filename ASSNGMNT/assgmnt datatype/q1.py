# WAP to get a string from a given string where all the occurances of it's first char have been $
#i/p = restart
# o/p = resta$t

str1 = "restart"
print("the string is :",str1)
str2 = str1[0]
str1 = str1.lower()
for i in range (1,len(str1)):
    if str1[i] == str1[0]:
        str2 = str2+"$"
    else:
        str2 = str2+str1[i]
print("the new string is : ",str2)