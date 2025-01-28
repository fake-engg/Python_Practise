# Inheritance template.
# We define parent class name in the brackets while declaring the child classes.

'''

class Phone:
    def __init__(self, price, brand, camera):
        print(f'Inside Phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print(f'Buying the phone')

    def return_phone(self):
        print(f'Returing the phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    pass

# p1 = Phone(25000,'HTC','13px')
# Phone(25000,'HTC','13px').buy()

# Even if we create object of SmartPhone class, Phone's constructor will be called automatically. As child class inherits Parent class's constructor.

s1 = SmartPhone(25000,'Apple','14px') #This will call Phone's constructor
s1.buy()    # Child object is accessing parent class method
s1.return_phone()

'''

#--- WHAT ALL CAN BE ACCESSED BY CHILD CLASS ---#
'''
1. Child class cannot directly access the private variables of the parent class
'''

'''

class Phone:
    def __init__(self, price, brand, camera):
        print(f'Inside Phone constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print(f'Buying the phone')

    def return_phone(self):
        print(f'Returing the phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def display(self):
        print(f'Brand is:{self.brand}')
        print(f'Price is:{self.__price}') # Since price is the private variable, Child class cannot access it directly and hence will throw an error

s1 = SmartPhone(25000,'Samsung','25px') # This will call the parent class constructor
s1.display()

'''


# LAST EXAMPLE SHOWED THAT WE CANNOT ACCESS PRIVATE VARIABLE OF PARENT CLASS FROM THE CHILD CLASS
# In order to access the private variables, we should create getter/setter methods in the parent class and then access the private variables from the child class using them

class Phone:
    def __init__(self, price, brand, camera):
        print(f'Inside Phone constructor')
        self.__price = price
        self.brand = brand
        self.camera = camera

    def set_price(self,price):
        self.__price = price

    def get_price(self):
        return self.__price

    def buy(self):
        print(f'Buying the phone')

    def return_phone(self):
        print(f'Returing the phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def display(self):
        print(f'Brand is:{self.brand}')
        # print(f'Price is:{self.__price}') 
        print(f'Price is: {self.get_price()}')

s1 = SmartPhone(25000,'Samsung','25px') 
s1.display()