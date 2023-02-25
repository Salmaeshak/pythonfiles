def calculator(func):
    def addition(a,b,op):
        if op == "+":
            print("the sum is ",a+b)
        elif op == "-":
            print("the difference is",a-b)
        elif op == "*":
            print("the product is",a*b)
            return
        return func(a,b,op)
    return addition
@calculator #print(calculator(div)
def div(a,b,op):
    if op == "/":
        print("the division is",a/b)
        return

div(4,5,"+")
div(5,6,"-")
div(2,4,"*")
div(10,2,"/")
