import unittest
from lesson3.enterprise.prepare_db import ClPrepareDB
from lesson3.enterprise.departments_core.DepartmentFactory import ClDepartmentFactory
from lesson3.enterprise.people_core.PeopleFactory import ClPeopleFactory
from lesson3.enterprise.employers_core.EmployerFactory import ClEmployerFactory
from lesson3.enterprise.enterprise import ClEnterprise


class ClTestEnterpriseMethods(unittest.TestCase):

    def test_create_enterprise(self):
        prepare_db = ClPrepareDB()
        prepare_db.prepare()
        db_name = 'enterprise.db'
        ent = ClEnterprise(db_name)
        self.assertTrue(ent.attributes[0][0] == 0)
        self.assertTrue(ent.attributes[0][1] == 'Title')
        self.assertTrue(ent.attributes[0][2] == 'The Continental')


class TestDepartmentFactoryMethods(unittest.TestCase):

  def test_create_department(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      dep_factory = ClDepartmentFactory(db_name)
      dept = dep_factory.add_department('Континенталь', 'Liverpool, UK')
      self.assertTrue(dep_factory.departments[0].get_name() == 'The Continental')
      self.assertTrue(dep_factory.departments[0].get_address() == 'New York City, USA')
      self.assertTrue(dep_factory.departments[1].get_name() == 'Континенталь')
      self.assertTrue(dep_factory.departments[1].get_address() == 'Liverpool, UK')

  def test_change_department(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      dep_factory = ClDepartmentFactory(db_name)
      dept = dep_factory.add_department('Континенталь', 'Liverpool, UK')
      dept = dep_factory.update_department_by_id(1, 'Континенталь', 'Brussels, Belgium')
      self.assertTrue(dep_factory.departments[0].get_name() == 'The Continental')
      self.assertTrue(dep_factory.departments[0].get_address() == 'New York City, USA')
      self.assertTrue(dep_factory.departments[1].get_name() == 'Континенталь')
      self.assertTrue(dep_factory.departments[1].get_address() == 'Brussels, Belgium')

  def test_delete_department(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      dep_factory = ClDepartmentFactory(db_name)
      dept = dep_factory.add_department('Континенталь', 'Liverpool, UK')
      dept = dep_factory.delete_department_by_id(1)
      self.assertTrue(dep_factory.departments[0].get_name() == 'The Continental')
      self.assertTrue(dep_factory.departments[0].get_address() == 'New York City, USA')


class TestPeopleFactoryMethods(unittest.TestCase):

  def test_create_people(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      people_factory = ClPeopleFactory(db_name)
      people = people_factory.add_people('Lesley', 'Wicked', 'Old Rascal', '01/01/1944', '1-123-432-6748')
      self.assertTrue(str(people_factory.people[1]),
                      str.format('Lesley Old Rascal Wicked, 01/01/1944, phone: 1-123-432-6748'))

  def test_change_people(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      people_factory = ClPeopleFactory(db_name)
      people = people_factory.add_people('Lesley', 'Wicked', 'Old Rascal', '01/01/1944', '1-123-432-6748')
      people = people_factory.update_people_by_id(1, 'Lesley', 'Wicked', 'The Hedgehog', '01/01/1944', '1-123-432-6748')
      self.assertTrue(str(people_factory.people[1]),
                      str.format('Lesley The Hedgehog Wicked, 01/01/1944, phone: 1-123-432-6748'))
  def test_delete_people(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      people_factory = ClPeopleFactory(db_name)
      people = people_factory.add_people('Lesley', 'Wicked', 'Old Rascal', '01/01/1944', '1-123-432-6748')
      people = people_factory.delete_people_by_id(1)
      self.assertTrue(len(people_factory.people), 1)


class TestEmployerFactoryMethods(unittest.TestCase):

  def test_create_employer(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      people_factory = ClPeopleFactory(db_name)
      dep_factory = ClDepartmentFactory(db_name)
      employers_factory = ClEmployerFactory(db_name)
      man = employers_factory.add_employer(people_factory.get_people_by_id(0), dep_factory.get_department_by_id(0),
                                           500000)
      self.assertTrue(len(employers_factory.employers), 2)

  def test_change_employer(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      people_factory = ClPeopleFactory(db_name)
      dep_factory = ClDepartmentFactory(db_name)
      employers_factory = ClEmployerFactory(db_name)
      man = employers_factory.add_employer(people_factory.get_people_by_id(0), dep_factory.get_department_by_id(0),
                                           500000)
      employers_factory.update_employer_by_id(1, dep_factory.get_department_by_id(0), 1000000)
      self.assertTrue(employers_factory.get_employer_by_id(1).get_salary(), 1000000)


  def test_delete_employer(self):
      prepare_db = ClPrepareDB()
      prepare_db.prepare()
      db_name = 'enterprise.db'

      people_factory = ClPeopleFactory(db_name)
      dep_factory = ClDepartmentFactory(db_name)
      employers_factory = ClEmployerFactory(db_name)
      man = employers_factory.add_employer(people_factory.get_people_by_id(0), dep_factory.get_department_by_id(0),
                                           500000)
      employers_factory.delete_employer_by_id(1)
      self.assertTrue(len(employers_factory.employers), 1)


if __name__ == '__main__':
    unittest.main()
