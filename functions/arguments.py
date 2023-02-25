"""parameters are the value the given in the time of function definition... the arguments are the value that given in the time of function call
** there are 5 arguments
1 positional arguments
2 arbitary arguments
3 keyword arguments
4 arbitary keyword arguments
5 default parameter value"""

#postitional argument
# def my_func(msg1,msg2):
#     print(msg1+" salma "+msg2)
# my_func("hai","how r you")

#arbitary arguments
# def my_func(*msg):
#     print("the first msg is",msg)
# my_func("hai","hello")

#keyword arguments
# def myfunc(child1,child2,child3):
#     print("second child name",child3)
# myfunc(child1="many",child2="ravi"child3="simi")

#arbitary keyword argument
# def my_func(**child):
#     print("the name of kids",child)
# my_func(child2 ="salma",child4="simi")

#default value parameters
def my_func(msg="hai hello"):
    print("the first msg is ",msg)

my_func()
