class A:
    def __init__(self,id,fname,lname,age,loc):
        self.id=id
        self.fn=fname
        self.ln=lname
        self.age=age
        self.loc=loc
    def printvalue(self):
        print(self.id,self.fn,self.ln,self.age,self.loc)
obj=A(101,'arun','k',22,'thr')
obj.printvalue()