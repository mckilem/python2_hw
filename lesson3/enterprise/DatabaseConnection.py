import sqlite3
import os

class ClDatabaseConnection: 

    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
        except Exception as e:
            print(e)
        
    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            print(e)         
    
    def rollback(self):
        try:
            self.conn.rollback()
        except Exception as e:
            print(e)        

    def close(self):
        try:
            self.conn.close()
        except Exception as e:
            print(e)        

    def dispose(self):
        self.conn.close()
    
    def execute_with_commit(self, sql, args):
        try:
            c = self.conn.cursor()
            c.execute(sql, args)
            self.commit()
        except Exception as e:
            print(e)

    def execute_no_commit(self, sql, args):
        try:
            c = self.conn.cursor()
            c.execute(sql, args)
            self.commit()
        except Exception as e:
            print(e)

    def get_cursor(self, sql, args):
        try:
            c = self.conn.cursor()
            c.execute(sql, args)
            return c
        except Exception as e:
            print(e)