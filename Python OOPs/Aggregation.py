# Template of HAS-A relationship

# Customer has a address. Hence, address attribute will be added to customer object and by that customer object will have full access to Address class.

'''
class Customer:
    def __init__(self,name,age,contact,address):
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address

    def view_details(self):
        pass

    def update_details(self):
        pass

class Address:
    def __init__(self,door,street,pincode):
        self.door = door
        self.street = street
        self.pincode = pincode 

    def update_address(self):
        pass
        
'''

# How to pass the Address attribute to the customer object

'''

class Customer:
    def __init__(self,name,age,contact,address):
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address

    def view_details(self):
        print("Showing Customer details...")
        print()
        print("Name:",self.name)
        print("Age:",self.age)
        print("contact:",self.contact)
        print("Address: ",self.address.door,self.address.street,self.address.pincode) # accessing the instance of the address class

    def update_details(self,add):
        self.address = add

class Address:
    def __init__(self,door,street,pincode):
        self.door = door
        self.street = street
        self.pincode = pincode 

    def update_address(self):
        pass

add1 = Address(123,'Steel Gate',828119)
add2 = Address(456,'Bank more',700001)

c1 = Customer('Shivam',26,7004088721,add1) # for c1 object, add1 is passed as the attribute for address class. And hence c1 has add1
c1.view_details()
c1.update_details(add2) # Address got updated for c1 and now it is add2.
c1.view_details()

'''


# ----- WHAT IF THE ADDRESS CLASS HAS PRIVATE VARIABLES -----# 

class Customer:
    def __init__(self,name,age,contact,address):
        self.name = name
        self.age = age
        self.contact = contact
        self.address = address

    def view_details(self):
        print("Showing Customer details...")
        print()
        print("Name:",self.name)
        print("Age:",self.age)
        print("contact:",self.contact)
        print("Address: ",self.address.get_door(),self.address.get_street(),self.address.get_pincode()) # accessing the instance of the address class

    def update_details(self,add):
        self.address = add

class Address:
    def __init__(self,door,street,pincode):
        self.__door = door
        self.__street = street
        self.__pincode = pincode 

    def get_door(self):
        return self.__door
    
    def get_street(self):
        return self.__street
    
    def get_pincode(self):
        return self.__pincode
    
    def set_door(self,value):
        self.__door = value

    def set_street(self,value):
        self.__street = value

    def set_pincode(self,value):
        self.__pincode = value 

    def update_address(self):
        pass

add1 = Address(123,'Steel Gate',828119)
add2 = Address(456,'Bank more',700001)

c1 = Customer('Shivam',26,7004088721,add1) # for c1 object, add1 is passed as the attribute for address class. And hence c1 has add1
# this is the line which makes it a strict relationship. because if we do not create a add1 object, c1 will throw an error. which means the 2 classes: Customer and Address has a strict relationship.
c1.view_details()
c1.update_details(add2) # Address got updated for c1 and now it is add2.
c1.view_details()

# Changing the values of private variables
add2.set_door('NU/78')
add2.set_street('NBCC Colony')
add2.set_pincode(828119)

c1.view_details()