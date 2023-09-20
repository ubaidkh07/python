class Person:
    def setvalue(self,fname,lname,age,loc):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.loc=loc
    def printvalue(self):
        print(self.fname)
        print(self.lname)
        print(self.age)
        print(self.loc)
obj=Person()
obj.setvalue("ayoob","ki",20,"thr")
obj.printvalue()