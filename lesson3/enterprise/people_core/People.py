class ClPeople:
    
    def __init__(self, id, fname, lname, nickname, date_of_birth, phone):
        self.id = id
        self.fname = fname
        self.lname = lname
        self.nickname = nickname
        self.date_of_birth = date_of_birth
        self.phone = phone
        
    # gets'n'sets

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id


    # end gets'n'sets section

    # private methods

    def __repr__(self):
        return str.format('{0} {2} {1}, {3}, phone: {4}', self.fname, self.nickname, self.lname, self.date_of_birth, self.phone)

    # common methods
