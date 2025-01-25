# product with 10% discount on each product
'''
def purchase(item, price):
    discount=10
    tot_price = price - price * discount/100
    return tot_price

print(purchase("Mobile",20000))
print(purchase("Shoe",1000))

'''
### OBSERVE THE CHANGE IN THE CODE 

# When: 
# If the mobile brand is 'Apple' then the discount is 10% else the discount is 5%
# All shoes have 2% tax and no discount

'''

def purchase(item, tot_price, brand='None'):
    if item=='Mobile':
        if brand =='Apple':
            discount=10  #deciding the discount value with respect to brand
        else:
            discount=5
        tot_price= tot_price - tot_price * discount/100 #once the discount is decided, we are calculating the tot_price
    else:
        tot_price = tot_price + 0.02 * tot_price
    return tot_price

print(purchase('Mobile',25000,'Apple'))
print(purchase('Mobile',15000,'Samsung'))
print(purchase('Shoe',8000))


'''

# Now if we want make any changes in the logics of Shoes price calculation then we are modifying the logics of
# mobile as well
# 
# Better to separate both the logics and do the changes separately

'''
def purchase_mobile(brand,price):
    if brand =='Apple':
        discount=10
        #print(type(discount))
    else:
        discount=5
    price = price - price * int(discount)/100
    print(f"Total price of {brand} mobile after discount of {discount}% is: {price}")
    
def purchase_shoe(price,material):
    if material == 'Leather':
        tax = 5
    else:
        tax = 2
    price = price + price * int(tax)/100
    print(f"Total price of the shoe after adding tax of {tax}% is: {price}")


purchase_mobile('Apple',55000)
purchase_mobile('Samsung',35700)
purchase_shoe(12000,'Seude')
purchase_shoe(19000,'Leather')

'''

# The above code can be written using OOPs. Where Mobile and Shoes are 2 different objects
# Mobile attributes: Brand, price
# Shoe attributes: Material, price
#Properties: Purchase, Return

class Mobile:
    def __init__(self, Brand, Price): # "Brand" and "Price" are the parameters name as passed while obj creation
        self.B = Brand  # name of the instance variable is 'B' and the paramenter name is 'Brand'
        self.P = Price

mob1 = Mobile('Apple', 35000)
print(f"Mobile has brand '{mob1.B}' and the price is: {mob1.P}") #invoking the instance variables



