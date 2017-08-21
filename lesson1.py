# 1.	Записать строку символов в текстовый файл и вывести содержимое файла.

new_file = open('test.txt', 'w')
new_file.write('qwertyuiopasdfghjk123456789')
new_file.close()

new_file = open('test.txt', 'r')
str_arr = new_file.read()
print(str_arr)

# 2.	Записать строку символов в файл, с явным указанием кодировки utf-8, вывести содержимое файла.
new_file = open('test1.txt', 'w', encoding='utf-8')
my_str = 'qwertyuiopasdfghjk123456789'
new_file.write(my_str)
new_file.close()

new_file = open('test1.txt', 'r')
str_arr = new_file.read()
print(str_arr)

# 3.	Декодировать содержимое файла из предыдущего задания.

new_file = open('test1.txt', 'rb')
str_arr = new_file.read()
my_str = str_arr.decode('utf-8')
print(my_str)

# 4.	Записать строку символов в двоичный файл и вывести содержимое файла.

new_file = open('test.txt', 'wb')
new_file.write(b'qwertyuiopasdfghjk123456789')
new_file.close()

new_file = open('test.txt', 'rb')
str_arr = new_file.read()
print(str_arr)


# 5.	Записать строку символов в файл, с явным указанием кодировки latin-1, вывести содержимое файла.

new_file = open('test1.txt', 'w', encoding='latin-1')
my_str = 'qwertyuiopasdfghjk123456789'
new_file.write(my_str)
new_file.close()

new_file = open('test1.txt', 'r')
str_arr = new_file.read()
print(str_arr)

# 6.	Декодировать содержимое файла из предыдущего задания.

new_file = open('test1.txt', 'rb')
str_arr = new_file.read()
my_str = str_arr.decode('latin-1')
print(my_str)

# 7.	*Определить, какой из txt-файлов был создан раньше всех.


from datetime import date
import time
import os


class ClImage:

    filename = ''
    dtt = time.time()

    def __init__(self, _filename, _date):
        self.filename = _filename
        self.dt = _date

    def __repr__(self):
        return repr((self.filename, time.strftime('%A, %d. %B %Y %I:%M%p', time.gmtime(self.dt))))

def get_images(directory):
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.jpg'):
                fileList.append(os.path.join(root, file))
                #  print os.path.join(root, file)
    return fileList

IMAGES_DIR = os.path.dirname(os.path.abspath(__file__)) + '/images'
images_array_with_dates = []
for file in get_images(IMAGES_DIR):
    filestat = os.stat(file)
    images_array_with_dates.append(ClImage(file, filestat.st_birthtime))
res = sorted(images_array_with_dates, key=lambda img: img.dt)
print(res[0])
