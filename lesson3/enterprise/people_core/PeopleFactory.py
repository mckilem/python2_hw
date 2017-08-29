from database_connection import ClDatabaseConnection
from people_core.People import ClPeople

class ClPeopleFactory:

    def __init__(self, db_name):
        self.db = ClDatabaseConnection(db_name)
        try:
            self.people = []
            cur = self.db.get_cursor('SELECT idField, first_name, last_name, nickname, date_of_birth, phone_number FROM tbl_people', ())
            rows = cur.fetchall()
            for row in rows:
                new_man = ClPeople(row[0], row[1], row[2], row[3], row[4], row[5])
                self.people.append(new_man)                
            cur.close()            
        except Exception as e:
            print(e)

    def get_people(self):
        return self.people
    
    def add_people(self, fname, lname, nickname, date_of_birth, phone):
        cur = self.db.get_cursor('SELECT max(idField) FROM tbl_people',())
        max_num = int(cur.fetchone()[0]) + 1
        cur.close()
        self.db.execute_with_commit('INSERT INTO tbl_people VALUES (:id, :fname, :lname, :nickname, :date_of_birth, :phone_number)', 
                                    (max_num, fname, lname, nickname, date_of_birth, phone))
        man = ClPeople(max_num, fname, lname, nickname, date_of_birth, phone)        
        self.people.append(man)  
        return man      

    def delete_people_by_id(self, id):
        man = self.get_people_by_id(id)
        self.db.execute_with_commit('DELETE FROM tbl_people WHERE idField = :id',(id,))
        self.people.remove(man)        

    def update_people_by_id(self, id, fname, lname, nickname, date_of_birth, phone):
        man = self.get_people_by_id(id)
        self.db.execute_with_commit('UPDATE tbl_people SET \
                                                first_name = :fname, \
                                                last_name = :lname, \
                                                nickname = :nickname, \
                                                date_of_birth = :date_of_birth, \
                                                phone_number = :phone_number \
                                                WHERE idField = :id',
                                    (fname, lname, nickname, date_of_birth, phone, id))
        man.fname = fname
        man.lname = lname 
        man.nickname = nickname
        man.date_of_birth = date_of_birth
        man.phone = phone

    def get_people_by_name(self, name):
        for man in self.people:
            if str.lower(name) == str.lower(man.name):
                return man
        return None
    
    def get_people_by_id(self, id):
        for man in self.people:
            if id == man.id:
                return man
        return None
    
    def __repr__(self):
        return str(self.people)