#average of two number
class A:
    def read(self):
        self.x = int(input("enter the number:"))
        self.y = int(input("enter the number:"))
class B(A):
    def sum(self):
        c = self.x+self.y
        print("the sum is :",c)
class C(B):
    def avrg(self):
        a = (self.x+self.y)/2
        print("the avrg is",a)
ob = C()
ob.read()
ob.sum()
ob.avrg()