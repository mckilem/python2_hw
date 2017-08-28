import sqlite3
import os

# todo по правильному работу с БД вынести бы в отдельное ядро
class ClLibrary(): 

    def __init__(self):
        try:
            self.conn = sqlite3.connect('library.db')
        except Exception as e:
            print(e)
        
    def _commit_(self):
        try:
            self.conn.commit()
        except Exception as e:
            print(e)         

    def _rollback_(self):
        try:
            self.conn.rollback()
        except Exception as e:
            print(e)        

    def _close_(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)        

    def dispose(self):
        self.conn.close()
    
    def print_authors(self):
        try:
            sql = 'SELECT idAUTHOR, First_name, Last_name FROM Author'
            c = self.conn.cursor()
            c.execute(sql)
            print('Список авторов')
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)

    def print_books(self):
        try:
            sql = 'SELECT B.NameB, B.YearB, B.Shelve, A.First_name, A.Last_name FROM Author A, Books B WHERE A.idAUTHOR=B.idAUTHOR'
            c = self.conn.cursor()
            c.execute(sql)
            print('Список книг')
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)

    def print_journals(self):
        try:
            sql = 'SELECT J.nameJ, J.YearJ, J.shelve, A.First_name, A.Last_name FROM Author A, journals J WHERE A.idAUTHOR=J.idAUTHOR'
            c = self.conn.cursor()
            c.execute(sql)
            print('Список журналов')
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)

    # adding elements
    def add_author(self, id, first_name, last_nasme):
        try:
            sql = 'INSERT INTO Author(idAUTHOR, First_name, Last_name)' \
                      ' VALUES(:id,:fname,:lname)'
            args = (id, first_name, last_nasme)
            c = self.conn.cursor()
            c.execute(sql, args)
            self._commit_()
        except Exception as e:
            print(e)

    def add_book(self,id, name, year, shelve, idauthor):
        try:
            sql = 'INSERT INTO Books(idBooks, NameB, YearB, Shelve, idAUTHOR)'\
                    ' VALUES(:idBooks, :NameB, :YearB, :Shelve, :idAUTHOR)'
            args=(id, name, year, shelve, idauthor)
            c = self.conn.cursor()
            c.execute(sql,args)
            self._commit_()
        except Exception as e:
            print(e)

    def add_journal(self,id, name, year, shelve, publisher, idauthor):
        try:
            sql = 'INSERT INTO Journals (idJournals, nameJ, yearJ, shelve, Publisher, idAUTHOR)'\
                    ' VALUES(:idJournals, :nameJ, :yearJ, :Shelve, :Publisher, :idAUTHOR)'
            args=(id, name, year, shelve, publisher, idauthor)
            c = self.conn.cursor()
            c.execute(sql,args)
            self._commit_()
        except Exception as e:
            print(e)

    # update elements
    def update_author(self, first_name, last_name, id):
        try:
            sql = 'UPDATE Author SET First_name = :fname, Last_name = :lname WHERE idAUTHOR = :id'
            c = self.conn.cursor()
            c.execute(sql,(first_name, last_name,id))
            self._commit_()
        except Exception as e:
            print(e)
    
    def update_book(self, name, id):
        try:
            sql = 'UPDATE Books SET NameB = :name WHERE idBooks = :id'
            c = self.conn.cursor()
            c.execute(sql,(name,id))
            self._commit_()
        except Exception as e:
            print(e)

    def update_journal(self, name, id):
        try:
            sql = 'UPDATE Journals SET NameJ = :name WHERE idJournals = :id'
            c = self.conn.cursor()
            c.execute(sql,(name,id))
            self._commit_()
        except Exception as e:
            print(e)
    
    # deleting elements
    def delete_author(self, id):
        try:
            sql = 'DELETE FROM Author WHERE idAUTHOR = :id'
            c = self.conn.cursor()
            c.execute(sql, (id,))
            self._commit_()
        except Exception as e:
            print(e)
    
    def delete_book(self, id):
        try:
            sql = 'DELETE FROM Books WHERE idBooks = :id'
            c = self.conn.cursor()
            c.execute(sql, (id,))
            self._commit_()
        except Exception as e:
            print(e)

    def delete_journal(self, id):
        try:
            sql = 'DELETE FROM Journals WHERE idJournals = :id'
            c = self.conn.cursor()
            c.execute(sql, (id,))
            self._commit_()
        except Exception as e:
            print(e)


    def search_book(self, name):
        try:
            sql = 'SELECT B.NameB, B.YearB, B.Shelve, A.First_name, A.Last_name FROM Author A, Books B WHERE A.idAUTHOR=B.idAUTHOR and B.NameB like \'%:name%\''
            c = self.conn.cursor()
            c.execute(sql, (name,))
            print('Список книг')
            rows = c.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)