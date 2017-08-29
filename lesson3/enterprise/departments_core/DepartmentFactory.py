from database_connection import ClDatabaseConnection
from departments_core.Department import ClDepartment

class ClDepartmentFactory:

    def __init__(self, db_name):
        self.db = ClDatabaseConnection(db_name)
        try:
            self.departments = []
            cur = self.db.get_cursor('SELECT idField, name, address FROM tbl_departments', ())
            rows = cur.fetchall()
            for row in rows:
                new_dep = ClDepartment(row[0], row[1], row[2])
                self.departments.append(new_dep)                
            cur.close()            
        except Exception as e:
            print(e)

    def get_departments(self):
        return self.departments
    
    def add_department(self, name, address):
        cur = self.db.get_cursor('SELECT max(idField) FROM tbl_departments',())
        max_num = int(cur.fetchone()[0]) + 1
        cur.close()
        self.db.execute_with_commit('INSERT INTO tbl_departments VALUES (:id, :name, :address)', 
                                    (max_num, name, address))
        department = ClDepartment(max_num, name, address)        
        self.departments.append(department)  
        return department      

    def delete_department_by_id(self, id):
        dept = self.get_department_by_id(id)
        self.db.execute_with_commit('DELETE FROM tbl_departments WHERE idField = :id',(id,))
        self.departments.remove(dept)        

    def update_department_by_id(self, id, name, address):
        dept = self.get_department_by_id(id)
        self.db.execute_with_commit('UPDATE tbl_departments SET name = :name, \
                                    address = :address WHERE idField = :id',
                                    (name, address, id))
        dept.name = name
        dept.address = address        

    def get_department_by_name(self, name):
        for dept in self.departments:
            if str.lower(name) == str.lower(dept.name):
                return dept
        return None
    
    def get_department_by_id(self, id):
        for dept in self.departments:
            if id == dept.id:
                return dept
        return None
    
    def __repr__(self):
        return str(self.departments)