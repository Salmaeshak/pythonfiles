class A:
    def emp(self):
        self.n = input("enter the employee name:")
        self.a = int(input("enter the age:"))
        self.ad = input("enter the adress:")
class B:
    def empsal(self):
        self.sal = int(input("enter the salary of the employee:"))
class C(A,B):
    def display(self):
       print("the employee detais are")
       print('name:',self.n,'\n age:',self.a,'\nadress:',self.ad,'\nsalary',self.sal)
ob = C()
ob.emp()
ob.empsal()
ob.display()