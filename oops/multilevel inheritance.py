class A:
    def printa(self,num1):
        self.n1=num1
        print("inside class A",self.n1)
class B(A):
    def printb(self,num2):
        self.n2=num2
        print("inside class B",self.n2)
class C(B):
    def printc(self,num3):
        self.n3=num3
        print("inside class C",self.n3)
obj=C()
obj.printa(30)
obj.printb(20)
obj.printc(40)