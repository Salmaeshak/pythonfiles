phy= int(input("enter the mark of physics "))
che = int(input("enter the mark of chemistry "))
bio = int(input("enter the mark of biology "))
math = int(input("enter the mark of mathematics "))
com = int(input("enter the mark of computer "))
percentage = ((phy+che+bio+math+com)/500)*100
print(percentage)
if percentage>=90:
    print("grade A")
elif percentage>=80:
    print("gade B")
elif percentage>=70:
    print("grade C")
elif percentage>=60:
    print("grade D")
elif percentage>=50:
    print("grade E")
elif percentage>=40:
    print("grade F")
else:
    print("fail")
    

