class ShoppingCart:
    def __init__(self, delivery_fees, discount):
        self.items = []
        self.delivery_fees = delivery_fees
        self.discount = discount
        self.total_amount = 0

    def addItem(self, item_name, item_price):
        self.items.append({'name': item_name, 'price': item_price})

    def removeItem(self, item_name):
        self.items = [item for item in self.items if item['name'].lower() != item_name.lower()]

    def selectDeliveryOption(self, delivery_option):
        if delivery_option == 'Standard':
            self.delivery_fees = 5
        elif delivery_option == 'Express':
            self.delivery_fees = 10

    def applyDiscount(self, discount_code):
        if discount_code == 'SAVE10':
            self.discount = 0.1
        elif discount_code == 'SAVE20':
            self.discount = 0.2
        else:
            self.discount = 0

    def calculateTotal(self):
        subtotal = sum([item['price'] for item in self.items])
        delivery_fees = self.delivery_fees
        discount = subtotal * self.discount
        self.total_amount = subtotal + delivery_fees - discount

    def checkOut(self):
        print("Shopping cart contents:")
        for item in self.items:
            print(f"- {item['name']} - {item['price']}")
        print(f'Delivery fees: {self.delivery_fees}')
        print(f'Discount: {self.discount * 100}%')
        print(f'Total amount: {self.total_amount}')



