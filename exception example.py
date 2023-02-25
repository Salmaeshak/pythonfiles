try:
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))
    n3 = num1/num2
    print("the output is:",n3)
# except ZeroDivisionError as er:
#     print(er)
# except ValueError as vr:
#     print(vr)
except Exception as ex:
    print(ex)