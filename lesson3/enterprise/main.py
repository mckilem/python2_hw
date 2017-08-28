import prepare_db
from departments_core.DepartmentFactory import ClDepartmentFactory

prepare_db = prepare_db.ClPrepareDB()
prepare_db.prepare()

db_name = 'enterprise.db'

#enteprise = ClEnterprise()

dep_factory = ClDepartmentFactory(db_name)
dept = dep_factory.add_department('Континенталь', 'Liverpool, UK')
print(dep_factory)
dep_factory.update_department_by_id(dept.id, dept.name, 'Brussels, Belgium')
print(dep_factory)
dep_factory.delete_department_by_id(dept.id)
print(dep_factory)
