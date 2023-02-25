"""1 write a python function to get max of 3 numbers
2 write a python function to sum all the numbers in list
3 write a python function to multiply all the numbers in a list"""
#1 QSTN
# def maxi(a,b,c):
#     print("the max of 3 numbers",max(a,b,c))
# num1 = int(input("enter the first number"))
# num2 = int(input("enter the second number"))
# num3 = int(input("enter the 3rd number"))
# maxi(num1,num2,num3)

#2 QSTN
# def sum(list1):
#     sum =0
#     for i in list1:
#         sum = sum+i
#     print("the sum of the list is",sum)
# my_list = [2,4,5,6,7,8]
# sum(my_list)

#3 QSTN
def multi(list1):
    prd = 1
    for i in list1:
        prd = prd*i
    print("the product of numbers in list ",prd)
my_list = [4,5,2,1,6,7,3]
multi(my_list)