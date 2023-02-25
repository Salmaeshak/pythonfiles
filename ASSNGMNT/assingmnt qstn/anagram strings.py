string1 = input("enter the first string :")
string2 = input("enter the second string :")
if len(string1) != len(string2):
    print("the strings are not anagram")
else:
    string1 = sorted(string1)
    string2 = sorted(string2)
    if string1 == string2:
        print("The strings are anagram")
    else:
        print("The strings are not anagram")
