str1 = str(input("enter a string: "))
revstr1 = str1[::-1]
if str1 == revstr1:
    print(str1,"is palindrome")
else:
    print(str1,"is not palindrome")