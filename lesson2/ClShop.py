from lesson2.ClProduct import ClProduct
from lesson2.ClFruitProduct import ClFruitProduct


class ClShop:
    def __init__(self, name, address, legal_info):
        self.name = name
        self.address = address
        self.employers = []
        self.products = []
        self.legal_info = legal_info
        self.earnings = 0

    # gets'n'sets
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_employers(self):
        return self.employers

    def get_products(self):
        return self.products

    def get_earnings(self):
        return self.earnings

    # end gets'n'sets section

    # shop methods

    def print_shop_info(self):
        print('Shop: ', self.name,
              '\r\nAddress: ', self.address,
              '\r\nLegal Info:', self.legal_info,
              '\r\nStuff count: ', len(self.employers),
              '\r\nProducts count: ', len(self.products))

    # working with employers

    def hire_employee(self, employee):
        if employee.check_self_correct:
            self.employers.append(employee)
        else:
            raise ValueError('Employee has incorrect information')  # по хорошему это надо проверить еще до этого места

    def fire_employee_by_name(self, employee_name):
        employee = self.find_employee_by_name(employee_name)
        if employee is not None:
            self.employers.remove(employee)

    def find_employee_by_name(self, name):
        for employee in self.employers:
            if employee.name == name:
                return employee
        return None

    def get_total_tips_earned(self):
        total_tips_earned = 0
        for employee in self.employers:
            total_tips_earned += employee.get_earnings()
        return total_tips_earned

        # working with products

    def add_product(self, product_name, price, quantity):

        if price < 0 or quantity < 0:
            raise ValueError('Price and Quantity should be positive')

        product = self.find_product_by_name(product_name)
        if product is None:
            product = ClProduct(product_name, price, quantity)
            self.products.append(product)
        else:
            product.update_price(price)
            product.add_quantity(quantity)
        return product

    def add_fruit(self, product_name, price, quantity, country_of_origin, expiration_date):

        if price < 0 or quantity < 0:
            raise ValueError('Price and Quantity should be positive')
        product = self.find_product_by_name(product_name)
        if product is None:
            product = ClFruitProduct(product_name, price, quantity, country_of_origin, expiration_date)
            self.products.append(product)
        else:
            product.update_price(price)
            product.add_quantity(quantity)
        return product

    def remove_product_by_id(self, product_id):
        product = self.find_product_by_id(product_id)
        if product is not None:
            self.products.remove(product)

    def find_product_by_id(self, id):
        for product in self.products:
            if product.uuid == id:
                return product
        return None

    def find_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def sell_product(self, product, quantity, employee):
        self.earnings += product.get_price() * quantity
        employee.add_tips(product.get_price() * quantity * 0.1)
        product.add_quantity(-1)
        if product.get_quantity() == 0:
            self.remove_product_by_id(product.uuid)

    # transaction log
    # todo So, every shop needs a transaction log

    # common methods
