from lesson3.enterprise.database_connection import ClDatabaseConnection
from lesson3.enterprise.employers_core.Employer import ClEmployer
from lesson3.enterprise.people_core.PeopleFactory import ClPeopleFactory
from lesson3.enterprise.departments_core.DepartmentFactory import ClDepartmentFactory

class ClEmployerFactory:

    def __init__(self, db_name):
        self.db = ClDatabaseConnection(db_name)
        try:
            people_factory = ClPeopleFactory(db_name)
            dept_factory = ClDepartmentFactory(db_name)
            self.employers= []
            cur = self.db.get_cursor('SELECT idField, id_people, id_department, salary FROM tbl_employers', ())
            rows = cur.fetchall()
            for row in rows:
                new_man = ClEmployer(row[0],
                                     people_factory.get_people_by_id(row[1]),
                                     dept_factory.get_department_by_id(row[2]),
                                     row[3])
                self.employers.append(new_man)
            cur.close()            
        except Exception as e:
            print(e)

    def get_employers(self):
        return self.employers
    
    def add_employer(self, people, department, salary):
        cur = self.db.get_cursor('SELECT max(idField) FROM tbl_employers',())
        max_num = int(cur.fetchone()[0]) + 1
        cur.close()
        self.db.execute_with_commit('INSERT INTO tbl_employers VALUES (:id, '
                                                                   ':people_id, '
                                                                   ':dept_id, '
                                                                   ':salary)',
                                    (max_num, people.id, department.id, salary))
        man = ClEmployer(max_num, people, department, salary)
        self.employers.append(man)
        return man      

    def delete_employer_by_id(self, id):
        man = self.get_employer_by_id(id)
        self.db.execute_with_commit('DELETE FROM tbl_employers WHERE idField = :id',(id,))
        self.employers.remove(man)

    def update_employer_by_id(self, id, department, salary):
        man = self.get_employer_by_id(id)
        self.db.execute_with_commit('UPDATE tbl_employers SET \
                                                id_department = :dept_id, \
                                                salary = :salary \
                                                WHERE idField = :id',
                                    (department.id, salary, id))
        man.department = department
        man.salary = salary

    def get_employer_by_name(self, name):
        for man in self.employers:
            if str.lower(name) == str.lower(man.name):
                return man
        return None
    
    def get_employer_by_id(self, id):
        for man in self.employers:
            if id == man.id:
                return man
        return None
    
    def __repr__(self):
        return str(self.employers)