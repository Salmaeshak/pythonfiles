#WAP for python function that takes a list of words and returns the length of the longest one

list1 = ["hai","salma","python","courses"]
firstwrd = list1[0]
temp = " "
lentemp = 0
for i in range(len(list1)):
    if len(list1[i]) > len(firstwrd):
        temp = list1[i]
        lentemp = len(list1[i])
        firstwrd = list1[i]
print("the longest wrd is",temp)
print("the length of longest wrd is",lentemp)
        