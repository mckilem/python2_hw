from lesson3.enterprise.people_core.People import ClPeople


class ClEmployer(ClPeople):
    
    def __init__(self, id, people, department, salary):
        super().__init__(people.id, people.fname, people.lname, people.nickname, people.date_of_birth, people.phone)
        self.id = id
        self.people = people
        self.department = department
        self.salary = salary        
        
    # gets'n'sets

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def get_salary(self):
        return self.salary


    # end gets'n'sets section

    # private methods

    def __repr__(self):
        return str.format('{0} with salary of {1} $', str(self.people), str(self.salary))

    # common methods
