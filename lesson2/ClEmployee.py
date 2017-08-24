import uuid


class ClEmployee:

    def __init__(self, name, date_of_birth, social_insurance_number):
        self.name = name
        self.uuid = uuid.uuid4()
        self.date_of_birth = date_of_birth
        self.social_insurance_number = social_insurance_number
        self.tips_earned = 0.0

    # gets'n'sets

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_uuid(self):
        return self.uuid

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_social_insurance_number(self):
        return self.social_insurance_number

    # end gets'n'sets section

    # employee methods

    def __repr__(self):
        return str.format('Name: {0}, Date of birth: {1}, Social security number: {2}',
                          self.name, self.date_of_birth, self.social_insurance_number)

    def add_tips(self, tips_amount):
        self.tips_earned += tips_amount

    def get_earnings(self):
        return self.tips_earned;

    def check_self_correct(self):
        # todo Need to add some logical tests for products
        return True

    # common methods
