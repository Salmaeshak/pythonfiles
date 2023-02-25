# reverse a string
def rev(str1):
    rev_str = str1[::-1]
    return rev_str
my_str = "1234abcd"
print("the sample string is : ",my_str)
print("the reverse of the string :",rev(my_str))