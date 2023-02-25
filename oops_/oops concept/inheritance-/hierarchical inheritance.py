#read sum avr product
class A:
    def read(self):
        self.x = int(input("enter the number:"))
        self.y = int(input("enter the number:"))
class B(A):
    def sum(self):
        s = self.x+self.y
        print("the sum is",s)
class C(A):
    def avrg(self):
        a = (self.x+self.y)/2
        print("the average is :",a)
class D(A):
    def prd(self):
        p = self.x*self.y
        print("the product is:",p)
ob1 = B()
ob1.read()
ob1.sum()
ob2 = C()
ob2.read()
ob2.avrg()
ob3 = D()
ob3.read()
ob3.prd()