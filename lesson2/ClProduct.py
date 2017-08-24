import uuid


class ClProduct:
    def __init__(self, name, price, initial_quantity):
        self.name = name
        self.uuid = uuid.uuid4()
        self.price = price
        self.quantity = initial_quantity

    # gets'n'sets

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_uuid(self):
        return self.uuid

    def get_price(self):
        return self.price

    def get_quantity(self):
        return self.quantity

    # end gets'n'sets section

    # product methods

    def __repr__(self):
        return str.format('{0}, Price: {1}, Quantity: {2}', self.name, self.price, self.quantity)

    def update_price(self, new_price):
        self.price = new_price

    def add_quantity(self, quantity):
        self.quantity += quantity

    def check_self_correct(self):
        # todo Need to add some logical tests for products
        return True

    # common methods
