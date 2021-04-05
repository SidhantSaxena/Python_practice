class Bank:
    def __init__(self,username,pin,total_amt):
        self.username = username
        self.pin = pin
        self.total_amt = total_amt
    
    
    def Credit(self,amount):
        self.total_amt+=amount
        print(f"{self.username}, {amount} has been credited, Total balance is {self.total_amt}")


    def Debit(self,amount):
        code = int(input("Please Enter your pin code : "))
        if code==self.pin:
            if self.total_amt>=amount:
                self.total_amt-=amount
                print(f"{self.username}, {amount} has been debited, Total balance is {self.total_amt}")
            else:
                print("Insufficient amount, you cannot withdraw")        
        else:
            print("Please try again")


p1 = Bank("sid",1234,12000)
print(p1.__dict__,"\n")
p1.Credit(20000)
money = int(input("Enter the amount you wish to withdraw : "))
p1.Debit(money)
print(p1.__dict__)