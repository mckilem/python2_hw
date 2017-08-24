from lesson2.ClProduct import ClProduct


class ClFruitProduct(ClProduct):
    def __init__(self, name, price, initial_quantity, country_of_origin, expiration_date):
        super().__init__(name, price, initial_quantity)
        self.country_of_origin = country_of_origin
        self.expiration_date = expiration_date

    # gets'n'sets

    def get_country_of_origin(self):
        return self.country_of_origin

    def get_expiration_date(self):
        return self.expiration_date

    # end gets'n'sets section

    # fruit methods

    def __repr__(self):
        return str.format('{0}, Country: {1}, Exp. date: {2}',
                          super().__repr__(), self.country_of_origin, self.expiration_date)

    def check_self_correct(self):
        # todo Need to add some logical tests for products
        return True

    # common methods
