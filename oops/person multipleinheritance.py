class Person:
    def personaldata(self,id,fname,lname,age):
        self.id=id
        self.fn=fname
        self.ln=lname
        self.age=age
class Address:
    def informationdata(self,district,country,phno):
        self.dis=district
        self.cntry=country
        self.phno=phno
class Employee(Person,Address):
    def professionaldata(self,qualification,prof,salary,exp):
        self.qual=qualification
        self.prof=prof
        self.salary=salary
        self.exp=exp
        print(self.id,self.fn,self.ln,self.age,self.phno,self.qual,self.prof,self.salary,self.exp,self.cntry)
obj=Employee()
obj.personaldata(101,'arshad','kh',20)
obj.informationdata('thrissur','india',9068724920)
obj.professionaldata('degree','developer',15000,'3year')