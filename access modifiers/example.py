class A:
    #public data member
    var1 = None
    #protected data member
    _var2 = None
    #private data member
    __var3 = None
#public memeber function
    def displaypublicmemebers(self):
        #access public memeber
        print("public data memeber:",self.var1)
#protected member function
    def _displayprotectedmembers(self):
        #access prortected member
        print("protected data member:",self._var2)
#private memeber function
    def __displayprivatemembers(self):
        print("private data memeber:",self.__var3)
#for access private member
    def accessprivatemember(self):
        self.__displayprivatemembers()

#derived class
class B(A):
    #constructor
    def __init__(self,var1,var2,var3):
        A.__init__(self,var1,var2,var3)
    #public memeber function
    def accessprotectmembers(self):
        #access protected member function of super class
         self._displayprotectedmembers()
#creating objects of the derived class
obj = B('pub_red','pro_red','private_green')
#calling public memeber function of the class
obj.displaypublicmemebers()
obj.accessprotectmembers()
obj.accessprivatemember()
#object can access public member
print("object is accessing public member:",obj.var1)
#object can access protected member
print("the object is accessing protected member:",obj._var2)
#object cannot access private member, so it will generate attribute error
print(obj._A__var3)#accessing name mangled variables