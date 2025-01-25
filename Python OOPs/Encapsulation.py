'''
class Customer:
    def __init__(self, name, age, walletBalance):
        self.name = name
        self.age = age
        self.walletBalance = walletBalance

    def update_balance(self, amount):
        self.walletBalance += amount

    def show_balance(self):
        print("Your current balance is:",self.walletBalance)


cus1 = Customer("Shivam",27,4000)

#simple transactions happening on normal days
cus1.show_balance()
cus1.update_balance(1500)
cus1.show_balance()

# Account hacked and certain amount is transferred to the account
cus1.walletBalance=500000
cus1.show_balance()

'''

# Since, walletBalance was a public variable and the scope of a public variable is outside of class as well.
# Now, walletBalance being a sensitive info should be kept private and hence we need to change the scope of this variable as private
# once a variable is kept private, it can only be accessed inside of a class


#---- CHANGED THE SCOPE OF WALLETBALANCE VARIABLE ------#

class Customer:
    def __init__(self, name, age, walletBalance):
        self.name = name
        self.age = age
        self.__walletBalance = walletBalance

    def update_balance(self, amount):
        self.__walletBalance += amount

    def show_balance(self):
        print("Your current balance is:",self.__walletBalance)


cus1 = Customer("Shivam",27,4000)

#simple transactions happening on normal days
cus1.show_balance()
cus1.update_balance(1500)
cus1.show_balance()

# Account hacked and certain amount is transferred to the account
cus1.walletBalance=500000 # After changing the scope, this line had no impact on the code. And the balance still remains the same.
# But one thing happened at the backend, this line created one more instance variable for cus1 object. as walletBalance variable doesnt exist.
# now our previously known walletBalance exists as _Customer__walletBalance i.e. _<class_name>__<variable_name>.

cus1.show_balance()

