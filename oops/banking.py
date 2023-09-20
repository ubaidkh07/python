class Bank:
    bank='punjabnationalbank'
    def accountcreate(self,name,accno):
        print('name=',name,'account number=',accno)
        self.minbalance=5000
        self.totalbalance=self.minbalance
        print("minbalance",self.minbalance,"totalbalance",self.totalbalance)
    def deposit(self,amount):
        self.totalbalance+=amount
        print("deposited",amount)
        print("balance",self.totalbalance)
    def withdraw(self,amount1):
        if(self.totalbalance<amount1):
            print("error")
        else:
            print("withdrawed",amount1)
            print("balance",self.totalbalance-amount1)
obj=Bank()
obj.accountcreate('arshad',12234)
obj.deposit(1500)
obj.withdraw(7000)
