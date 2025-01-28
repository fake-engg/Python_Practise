# --- METHOD OVERRIDING --- #
# Functions with the same name in parent as well as Child class.

'''

class Phone:
    def __init__(self,price,brand,camera):
        print(f'Inside Phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print(f'Buying a Phone')

    def return_phone(self):
        print(f'Returing a Phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):  #overridden method
        print(f'Buying a Smart Phone..')

s1 = SmartPhone(25000,'Samsung','25px')
s1.buy()    # Object of child class can simply access the overridden method.

'''

# WHAT IF THE OBJECT WANTS TO ACCESS THE OVERRIDDEN METHOD OF PARENTS CLASS

'''

class Phone:
    def __init__(self,price,brand,camera):
        print(f'Inside Phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print(f'Buying a Phone without camera')

    def return_phone(self):
        print(f'Returing a Phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def buy(self):  #overridden method
        super().buy()   # Parent method is called using super(). Using this, we can inherit some of the parent's characteristics and add child's in the following line of code
        print(f'Buying a Smart Phone with camera and wifi..')
        

s1 = SmartPhone(25000,'Samsung','25px')
s1.buy()    # Object of child class can simply access the overridden method.

'''


# --- NEED OF CONSTRUCTOR OVERRIDING ---#

#  Requirement: We want to initialize the child class attributes using constructor.

#  Problem: Once child class has its own constructor, it cannot inherit the parent class constructor and its attributes.

'''

class Phone:
    def __init__(self,price,brand,camera):
        print(f'Inside Phone constructor')
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print(f'Buying a Phone')

    def return_phone(self):
        print(f'Returing a Phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, os, ram):
        print(f'Inside SmartPhone constructor')
        self.os = os
        self.ram = ram

    def buy(self):
        super().buy()
        print(f'Buying a SmartPhone')

s = SmartPhone('Android',8)
print(s.os)
print(s.brand)  # this line will throw an error. 'SmartPhone' object has no attribute 'brand'

# This is because now the child class has its own constructor and hence Phone class constructor is not inhertied.
# Also, the attributes of the parent class are not inherited.


'''


# --- IMPT: HOW TO INHERIT PARENT CLASS ATTRIBUTES WHEN THE CHILD CLASS HAS IT'S OWN CONSTRUCTOR ??? ---- #

#Note: In such cases, we need to override the parent class constructor as well.

class Phone:
    def __init__(self, price,brand,camera):
        print(f'Inside Parent class constructor')
        self.price = price
        self.brand = brand
        self.camera = camera
    
    def buy(self):
        print(f'Buying a Phone')

    def return_phone(self):
        print('Returing a Phone')

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, price,brand,camera,os,ram):
        print('Inside Child class constructor')
        super().__init__(price,brand,camera)    # we do not pass 'self' argument while overriding the constructor
        self.os = os
        self.ram = ram
        

    def buy(self):
        print('Buying a Smartphone')
        super().buy()

s = SmartPhone(75000,'Apple','16px','iOS',8)

s.buy()
print(s.os)
print(s.brand)

'''
#Flow of values

--> Child Attributes initialised while Object creation >> Values go to Child class constructor >> Parent class constructor gets the value >> Parent class constructor get inherited and so do the parent class attributes

'''

