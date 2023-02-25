#oops
#class - object
class Emp:
    x = 100
    def display(self):
        print("simple fuction")
    def sum(self,a,b):
        print("the sum is :",a+b)
    def product(self,a,b):
        print("the product is:",a*b)
    # def dis():#without self arguments
    #     print("without self argument")
obj = Emp()
obj.display()
print("the value of x is:",obj.x)
obj.sum(30,40)
obj.product(2,4)
# ob = Emp #call class name without function bracket
# ob.dis()

class Dis:
    def read(self,a,b):
        self.x = a
        self.y = b
    def sum(self):
        print("the sum is:",self.x+self.y)
    def product(c):
        print("the product:",c.x*c.y)
obj = Dis()
obj.read(2,3)
obj.sum()
obj.product()

class Dos:
    def read(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        print("the sum is:",self.a+self.b)
obj = Dos()
obj.read(4,3)
obj.sum()


