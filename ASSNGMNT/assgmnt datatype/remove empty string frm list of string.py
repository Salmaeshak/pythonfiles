str1 = ["John","","Jack","Emma","","Jins","Lina"]
print("the list of string is",str1)
i = 0
while i<len(str1):
    if len(str1[i])==0:
        str1.pop(i)
    i = i+1
print("the list after removing the empty string",str1)