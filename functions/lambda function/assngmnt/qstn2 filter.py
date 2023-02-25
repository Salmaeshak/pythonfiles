"""using lambda function filter even numbers frm list of numbers"""
num =[2,5,6,7,9,8]
eve_num = list(filter(lambda a : a%2==0,num))
print(eve_num)

#odd
odd_num = list(filter(lambda a : a%2!=0,num))
print(odd_num)
