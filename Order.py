class Order:
    def __init__(self, date, shopping_cart, delivery_address, payment_method):
        self.date = date
        self.status = "Pending"
        self.shopping_cart = shopping_cart
        self.delivery_address = delivery_address
        self.payment_method = payment_method

    def validatePayment(self):
        # Check payment validity
        print("Payment validated.")

    def cancel(self):
        self.status = "Cancelled"
        print("Order cancelled.")

    def dispatch(self):
        if self.status == "Pending":
            self.status = "Dispatched"
            print("Order dispatched.")
        else:
            print("Order can only be dispatched when in 'Pending' status.")

    def confirmDelivery(self):
        if self.status == "Dispatched":
            self.status = "Delivered"
            print("Order delivered.")
        else:
            print("Order can only be confirmed when in 'Dispatched' status.")

    def refund(self):
        if self.status == "Delivered":
            self.status = "Refunded"
            print("Order refunded.")
        else:
            print("Order can only be refunded when in 'Delivered' status.")

    def archive(self):
        self.status = "Archived"
        print("Order archived.")

