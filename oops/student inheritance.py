class Student:
    def prsdata(self,id,fname,lname,age,loc):
        self.id=id
        self.fn=fname
        self.ln=lname
        self.age=age
        self.loc=loc
class Education(Student):
    def academicdata(self,sub1,sub2,sub3):
        self.s1=sub1
        self.s2=sub2
        self.s3=sub3
        print(self.id,self.fn,self.ln,self.age,self.s1,self.s2,self.s3,self.s1+self.s2+self.s3,self.loc)
obj=Education()
obj.prsdata(101,'ayoob','ki',20,'thr')
obj.academicdata(30,40,50)