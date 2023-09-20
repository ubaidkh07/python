class Person:
    def personaldata(self,id,fname,lname,age,loc):
        self.id=id
        self.fn=fname
        self.ln=lname
        self.age=age
        self.loc=loc
class Employee(Person):
    def profdata(self,qualification,dept,prof,salary):
        self.qual=qualification
        self.dept=dept
        self.prof=prof
        self.sal=salary
        print(self.id)
        print(self.fn)
        print(self.ln)
        print(self.age)
        print(self.qual)
        print(self.dept)
        print(self.prof)
        print(self.sal)
        print(self.loc)
obj=Employee()
obj.personaldata(101,'ayoob','ki',20,'thr')
obj.profdata('degree','flutter','developer',1000)
