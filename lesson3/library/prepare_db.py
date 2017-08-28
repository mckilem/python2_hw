import sqlite3
import os

class ClPrepareDB():

    def __init__(self):
        None

    def prepare(self):
        if os.path.exists('library.db'):
            os.remove('library.db')

        conn = sqlite3.connect('library.db')

        cur = conn.cursor()

        sql = 'CREATE TABLE Author                          \
            (                                             \
                idAUTHOR INTEGER NOT NULL PRIMARY KEY,    \
                First_name CHAR(32),                      \
                Last_name CHAR(32)                        \
            )'
        cur.execute(sql)

        sql = 'CREATE TABLE Books                           \
            (                                             \
                idBooks INTEGER NOT NULL PRIMARY KEY,     \
                NameB CHAR(100),                          \
                YearB INTEGER,                            \
                Shelve INTEGER,                           \
                idAUTHOR INTEGER NOT NULL,                \
                FOREIGN KEY (idAUTHOR) REFERENCES Author(idAUTHOR)\
            )'
        cur.execute(sql)

        sql = 'CREATE TABLE Journals                        \
            (                                             \
                idjournals INTEGER NOT NULL PRIMARY KEY,  \
                nameJ CHAR(32),                           \
                yearJ INTEGER,                            \
                shelve INTEGER,                           \
                Publisher CHAR(32),                       \
                idAUTHOR INTEGER NOT NULL,                \
                FOREIGN KEY (idAUTHOR) REFERENCES Author(idAUTHOR)\
            )'
        cur.execute(sql)

        conn.commit()

        cur.execute('INSERT INTO Author VALUES (1, "Маргарет", "Митчелл")')
        cur.execute('INSERT INTO Author VALUES (2, "Александр", "Пушкин")')
        cur.execute('INSERT INTO Author VALUES (3, "Антон", "Чехов")')

        cur.execute('INSERT INTO Books VALUES (1, "Унесенные ветром", 1943, 50, 1)')
        cur.execute('INSERT INTO Books VALUES (2, "Пиковая дама", 1919, 5, 2)')
        cur.execute('INSERT INTO Books VALUES (3, "Сборник стихов", 1960, 10, 2)')
        cur.execute('INSERT INTO Books VALUES (4, "Человек в футляре", 1980, 6, 3)')

        cur.execute('INSERT INTO Journals VALUES (1, "Современник", 1860, 11, "Санкт-Петербург", 2)')
        cur.execute('INSERT INTO Journals VALUES (2, "Стрекоза", 1880, 51, "Москва", 3)')

        print('База данных подготовлена для работы')

        conn.commit()
        conn.close()
