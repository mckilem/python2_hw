import prepare_db
from departments_core.DepartmentFactory import ClDepartmentFactory
from people_core.PeopleFactory import ClPeopleFactory
from employers_core.EmployerFactory import ClEmployerFactory
import enterprise

prepare_db = prepare_db.ClPrepareDB()
prepare_db.prepare()

db_name = 'enterprise.db'

ent = enterprise.ClEnterprise(db_name)
print(ent)

dep_factory = ClDepartmentFactory(db_name)
dept = dep_factory.add_department('Континенталь', 'Liverpool, UK')
print(dep_factory)
dep_factory.update_department_by_id(dept.id, dept.name, 'Brussels, Belgium')
print(dep_factory)
dep_factory.delete_department_by_id(dept.id)
print(dep_factory)


people_factory = ClPeopleFactory(db_name)
man = people_factory.add_people('Lesley', 'Wicked', 'Old Rascal', '01/01/1944', '1-123-432-6748')
print(people_factory)
people_factory.update_people_by_id(man.id, man.fname, man.lname, 'The Hedgehog', man.date_of_birth, man.phone)
print(people_factory)
people_factory.delete_people_by_id(man.id)
print(people_factory)


employers_factory = ClEmployerFactory(db_name)
man = employers_factory.add_employer(people_factory.get_people_by_id(0), dep_factory.get_department_by_id(0), 500000)
print(employers_factory)
employers_factory.update_employer_by_id(man.id, dep_factory.get_department_by_id(2), 1000000)
print(employers_factory)
employers_factory.delete_employer_by_id(man.id)
print(employers_factory)