from database_connection import ClDatabaseConnection
import os

class ClPrepareDB:

    def __init__(self):
        None

    def prepare(self):
        if os.path.exists('enterprise.db'):
            os.remove('enterprise.db')

        db = ClDatabaseConnection('enterprise.db')

        sql = 'CREATE TABLE tbl_enterprise_info \
            ( \
                idField INTEGER NOT NULL PRIMARY KEY, \
                field_name CHAR(255), \
                value CHAR(255) \
            )'
        db.execute_with_commit(sql, ())

        sql = 'CREATE TABLE tbl_people \
            ( \
                idField INTEGER NOT NULL PRIMARY KEY, \
                first_name CHAR(100),  \
                last_name CHAR(100), \
                nickname CHAR(100), \
                date_of_birth DATETIME, \
                phone_number CHAR(100) \
            )'
        db.execute_with_commit(sql, ())

        sql = 'CREATE TABLE tbl_departments \
            ( \
                idField INTEGER NOT NULL PRIMARY KEY, \
                name CHAR(100),  \
                address CHAR(100) \
            )'
        db.execute_with_commit(sql, ())

        sql = 'CREATE TABLE tbl_employers \
            ( \
                idField INTEGER NOT NULL PRIMARY KEY, \
                id_people INTEGER NOT NULL, \
                id_department INTEGER NOT NULL, \
                salary FLOAT NULL, \
                FOREIGN KEY (id_people) REFERENCES tbl_people(idField), \
                FOREIGN KEY (id_department) REFERENCES tbl_departments(idField) \
            )'
        db.execute_with_commit(sql, ())

        # filling main information
        db.execute_with_commit('INSERT INTO tbl_enterprise_info VALUES (0, "Title", "The Continental")', ())
        db.execute_with_commit('INSERT INTO tbl_enterprise_info VALUES (1, "Owner", "Winston")', ())
        db.execute_with_commit('INSERT INTO tbl_enterprise_info VALUES (2, "Concierge", "Charon")', ())

        # filling people
        db.execute_with_commit('INSERT INTO tbl_people VALUES (0, "John", "Wick", "Baba Yaga", 1964, "1-123-432-6748")', ())
        db.execute_with_commit('INSERT INTO tbl_people VALUES (1, "Winston", "", "The Owner", 1943, "1-123-555-4356")', ())
        db.execute_with_commit('INSERT INTO tbl_people VALUES (2, "Charon", "", "The Concierge", 1964, "1-123-555-4350")', ())

        # filling departments
        db.execute_with_commit('INSERT INTO tbl_departments VALUES (0, "The Continental", "New York City, USA")', ())
        db.execute_with_commit('INSERT INTO tbl_departments VALUES (1, "The Continental", "Brno, Czech Republic")', ())
        db.execute_with_commit('INSERT INTO tbl_departments VALUES (2, "The Continental", "Oslo, Norway")', ())
        db.execute_with_commit('INSERT INTO tbl_departments VALUES (3, "The Continental", "Rome, Italy")', ())

        # filling staff
        db.execute_with_commit('INSERT INTO tbl_employers VALUES (1, 1, 1, 50000)', ())

        print('db is redy for testing')

        db.dispose()