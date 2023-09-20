class Employee:
    cmpny='samsung'
    def setval(self,id,fname,lname,age,prof):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
    def printval(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,Employee.cmpny)
obj=Employee()
obj1=Employee()
obj2=Employee()
obj.setval(101,"ayoob","ki",20,"designer")
obj1.setval(102,"musthafa","p",21,"developer")
obj2.setval(103,"kiran",'k',22,"designer")
obj.printval()
obj1.printval()
obj2.printval()
