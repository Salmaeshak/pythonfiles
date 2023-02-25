"""WAP to print charcters fromm string that are even indexed"""
str1 = input("enter a string")
print("the string is :",str1)
length = len(str1)
print("the even indexed characters are:")
for i in range (0,length,2):
    print(str1[i])