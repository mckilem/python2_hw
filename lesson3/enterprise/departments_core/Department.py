class ClDepartment:
    
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address
        
    # gets'n'sets

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    # end gets'n'sets section

    # private methods

    def __repr__(self):
        return str.format('{0}, {1}', self.name, self.address)

    # common methods
