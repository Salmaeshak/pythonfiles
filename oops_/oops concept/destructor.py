class A:
    def __init__(self):
        print("non parametarized")
    def __del__(self):
        print("destructor")
    def display(self):
        print("hai")
ob = A()
ob.display()