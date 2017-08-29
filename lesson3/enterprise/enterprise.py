from database_connection import ClDatabaseConnection

class ClEnterprise:
    def __init__(self, db_name):
        self.db = ClDatabaseConnection(db_name)
        try:
            self.attributes = []
            cur = self.db.get_cursor('SELECT idField, field_name, value FROM tbl_enterprise_info', ())
            rows = cur.fetchall()
            for row in rows:
                new_attr = [row[0],row[1], row[2]]
                self.attributes.append(new_attr)
            cur.close()
        except Exception as e:
            print(e)

    def __repr__(self):
        return str(self.attributes)