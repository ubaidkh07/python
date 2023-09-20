class Student:
    clg='MES'
    def setval(self,id,fname,lname,age):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
    def printval(self):
        print(self.id)
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(Student.clg)
obj=Student()
obj.setval(1,"ayoob","ki",20)
obj.printval()
obj1=Student()
obj2=Student()
obj1.setval(2,"musthafa","p",21)
obj2.setval(3,"kiran","k",22)
obj1.printval()
obj2.printval()