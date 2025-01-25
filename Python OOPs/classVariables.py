# Accessing the class variables from inside and outside of the class

'''

class Mobile:
    discount = 20
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand

    def purchase(self):
        total = self.price - self.price * Mobile.discount/100
        print(f"Price of the mobile after the discount of {Mobile.discount}% is:", total)

print(f'Discount on the purchase of mobiles is:{Mobile.discount}')

m1 = Mobile(20000,'Apple')
m1.purchase()
m2 = Mobile(20000,'Samsung')
m2.purchase()

Mobile.discount = 50 # accessing the class variable from outside the class

m3 =Mobile(50000,'Apple')
m3.purchase()
m4 =Mobile(40000,'OnePlus')
m4.purchase()

'''


# Since discount is a senstive data, hence we should keep it as private

class Mobile:
    __discount = 20
    def __init__(self, price, brand):
        self.price = price
        self.brand = brand
    
    @classmethod
    def set_discount(cls,discount):
        cls.__discount = discount

    @classmethod
    def get_discount(self):
        return self.__discount 
    
    def purchase(self):
        total = self.price - self.price * self.get_discount()/100
        print(f"Price of the mobile of brand '{self.brand}' after the discount of {self.get_discount()}% is: {total}")


m1 = Mobile(20000,'Apple')
m1.purchase()
m2 = Mobile(20000,'Samsung')
m2.purchase()

#Mobile.discount = 50 
# accessing the class variable from outside the class. In this case, this line doesn't have any impact over the code.
# as the discount variable is now private.

print("Diwali Sale..")
Mobile.set_discount(50) #discount can now only be modified using setter method
# this line wouldn't work, if we don't declare the setter method as @classmethod and throw an error.
# once we define the setter method as @classmethod, then the value can be set for all the object at once.

#How declaring getter and setter as @classmethod helped us:
# Once we declare the getter and setter as @classmethod, we can now see that the value set by setter is now shared by all the objects.



m3 =Mobile(50000,'Apple')
m3.purchase()
m4 =Mobile(40000,'OnePlus')
m4.purchase()
