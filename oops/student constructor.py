class Student:
    def __init__(self,id,fname,lname,age,subject):
        self.id=id
        self.fn=fname
        self.ln=lname
        self.age=age
        self.sub=subject
    def printvalue(self):
        print(self.id,self.fn,self.ln,self.age,self.sub)
obj=Student(101,'ayoob','ki','18','maths')
obj1=Student(102,'musthafa','p',19,'social')
obj2=Student(103,'kiran','k',20,'chemistry')
obj.printvalue()
obj1.printvalue()
obj2.printvalue()