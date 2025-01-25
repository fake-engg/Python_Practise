class Account:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance

    def debitAmt(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!!")
        else:
            self.balance -=amount
            print(f"Amount debited is: {amount}")

    def creditAmt(self,amount):
        self.balance += amount
        print(f"Amount credited: {amount}")

    
    def showBalance(self):
        print(f"Current Balance: {self.balance}")

c1 = Account(577808,2500)
c2 = Account(577809,11500)
c3 = Account(577810,500)

# c3.debitAmt(1000)
# c3.showBalance()
# c1.creditAmt(1550)
# c1.showBalance()
c2.debitAmt(3700)
c2.creditAmt(3227)
c2.showBalance()
print(c2.__dict__)

# print(list.__dict__)
        
        