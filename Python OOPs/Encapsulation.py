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

'''

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

'''

#-------------------END---------------------#

# Encapsulation - exercise

class Student:
    def __init__(self, student_id=None,marks=None,age=None):
        self.__student_id=None
        self.__marks = None
        self.__age =None

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
    def set_id(self, student_id):
        self.__student_id = student_id

    def get_id(self):
        return self.__student_id
    
    def set_age(self,age):
        self.__age = age

    def get_age(self):
        return self.__age
    
    def validate_marks(self):
        if self.get_marks() >=0 and self.get_marks()<=100:
            return True
        else:
            return False
    def validate_age(self):
        if self.get_age()>20:
            return True
        else:
            return False
       
    def check_qualification(self):
        if self.validate_marks() ==True:
            if int(self.get_marks()) >= 65:
                return True
            else:
                return False
        else:
            return False
        
s1 = Student()
print("Student 1")
s1.set_id(101)
s1.set_marks(87)
s1.set_age(27)
print(s1.check_qualification())

print()
print("Student 2")

s2 = Student()
s2.set_id(102)
s2.set_marks(61)
s2.set_age(25)
print(s2.check_qualification())

        


