#non parameterized
class A:
    def __init__(self):
        print("non parameterized constuctor")
ob = A()

#parametarized
class A:
    def __init__(self,name):
        print("parameterized")
        self.na = name
    def display(self):
        print("name is",self.na)
ob = A("salma")
ob.display()
