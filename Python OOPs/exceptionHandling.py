class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance
class Customer:
    def __init__(self,cards):
        self.cards=cards
        print('Inside Constructor')
        # print(self.cards)
    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception()
        if card_no not in self.cards:   #checking if the customer has valid cards
            raise Exception()
        if price>self.cards[card_no].balance:   # this line is nothing but self.<card_object>.balance. this is how we access the CreditCard attributes using Customer object.
            raise Exception()
card1=CreditCard(101,800)
card2=CreditCard(102,2000)
cards={card1.card_no:card1,card2.card_no:card2}
# print(cards)
c=Customer(cards)   #initialising cards for customer object. this is an example of association relationship. Since 'c' customer object has both the cards card1 and card2 that's why we have created a dictionary.
while(True):
    card_no=int(input("Please enter a card number: "))
    price = int(input('Enter the amount: '))
    try:
        c.purchase_item(price,card_no)
        print('Remaining balance: ',(card1.balance - price))
        break
    except Exception as e:
        print("Something went wrong. ",str(e))
        print(type(e))
