"""two types of polymorphism
*compile time(function overloading)
*run time(function overidind)"""
#example for python supporting compile time
class A:
    def display(self,name = None):
        if name == None:
            print("hello")
        else:
            print("hello"+name)
ob = A()
ob.display()
ob.display("salma")

#example of run time
class Rectangle():
    def area(self,l,b):
        print("the area of rectangle is ",l*b)
class Square(Rectangle):
    def area(self,l,b):
        print("the area of square is :",l*b)
ob = Square()
ob.area(10,20)