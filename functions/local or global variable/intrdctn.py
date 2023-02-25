# #local variable
# def f():
#     s = "hai salma" #local variable
#     print(s)
# f()
#
# #global variable
# def g():
#     print("inside function:",s)
# s = "hai hello how r u" #global variable
# g()
# print("outer function:",s)
#non local
def program():
    def python():
       # nonlocal name #nonlocal give varaiable to access inside the main function
        name = "salma"
    def flutter():
        name = "ardeshir"
    def mean_stack():
        global name #global is give access to the variable out side the function
        name = "amina"
    name = "eshak"
    python()
    mean_stack()
    print("the coder is : ",name)

program()
print("name is :",name)