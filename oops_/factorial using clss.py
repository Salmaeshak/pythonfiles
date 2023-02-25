"""the factorial of a number using class with function argument and return"""
class Fact:
    def factorial(self,n):
        f=1
        for i in range(1,n+1):
            f = f*i
        return f
obj = Fact()
n = int(input("enter the number:"))
res = obj.factorial(n)
print("the factorial is",res)

#using recursion
class Fact:
    def factorial(self,n):
        if n == 1:
            return n
        else:
            return n*self.factorial(n-1)
obj = Fact()
n = int(input("enter the number:"))
f = obj.factorial(n)
print("the factorial is ",f)

