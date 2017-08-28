from prepare_db import ClPrepareDB
from ClLibrary import ClLibrary

prepare_db = ClPrepareDB()
prepare_db.prepare()

library = ClLibrary()
library.print_authors()
library.print_books()
library.print_journals()
print()

library.add_author(4, 'Джоан', 'Роулинг')
library.add_book(5,'Гарри Поттер и Философский камень', 2005, 6, 4)
library.add_author(5, 'Петр', 'Валиев')
library.add_journal(3, 'Хакер', 1999, 15, 'Хакер Пресс', 5)

library.print_authors()
library.print_books()
library.print_journals()
print()

library.update_author('Гарри', 'Поттер', 1)
library.update_book('Гарри Поттер и Орден Феникса', 5)
library.update_journal('Игромания',3)

library.print_authors()
library.print_books()
library.print_journals()
print()


library.delete_author(4)
library.delete_book(2)
library.delete_journal(3)

library.print_authors()
library.print_books()
library.print_journals()
print()

library.dispose()