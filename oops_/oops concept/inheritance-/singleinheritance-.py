# #single inheritance
# class A:
#     def displayA(self):
#         print("base class method")
# class B(A):
#     def displayB(self):
#         print("derived class method")
# ob = B()
# ob.displayA()
# ob.displayB()

#read two values and get sum using single inheritance
class A:
    def read(self,x,y):
        self.x = x
        self.y = y
class B(A):
    def sum(self):
        c = self.x+self.y
        print("the sum is :",c)
ob = B()
ob.read(3,4)
ob.sum()