def get_sum(num):
    if num==1:
        return num
    return num + get_sum(num-1)
num = int(input("enter a number : "))
print(get_sum(num))