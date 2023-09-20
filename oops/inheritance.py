class A:
    def printa(self,num1):
        self.num1=num1
        print(self.num1)
class B(A):
    def printb(self,num2):
        self.num2=num2
        print(self.num2)
obj=A()
obj.printa(10)
obj1=B()
obj1.printb(20)
obj1.printa(30)