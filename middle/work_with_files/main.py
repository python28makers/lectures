""" Работа с файлами """

# Операции над файлами:
# 1. Чтение файлов
# 2. Запись данных в файлы

# файлы бывают текстовые и бинарные

# open('путь_до_файла', 'режим_работы_с_файлом') - открывает файл, возвращает специальный тип данных для работы с файлом

# file = open('text1.txt', 'r')
# print(type(file))
# print(dir(file))
# # print(file.read())
# file.close()

# file.read() # ValueError - поскольку файл закрыт

"""  
Режимы работы с файлами
r (read) - чтение
w (write) - запись. Если файла НЕ существует - создает файл, если существует - перезаписывает содержимое
a (append) - запись, дозаписывает данные
x (exclusive) - создает файл и записывает. Если файл существует - вызывает исключение FileExistsError
b - открывает бинарные файлы (wb, rb)
t - открывает текстовые файлы (rt, wt)
+
r+, w+ - запись и чтение
"""


""" чтение """
# file = open('text1.txt', 'r')
# # print(file.read())  - возвращает содержимое файла в виде str. Можно указать количество символов
# file.close()

# file = open('text1.txt', 'r')
# print(file.readline()) # возвращает содержимое одной строки из файла
# print(file.readline())
# print(file.readline())
# file.close()

# file = open('text1.txt')
# print(file.readlines()) # возвращает все строки из файла в списке
# file.close()

# file = open('text1.txt', 'r')
# for string in file:
#     print(string)
# file.close()

""" запись """
# file = open('text2.txt', 'w')
# file.write("Завтра будет 5 апреля") # записывает строку в файл
# file.close()


# file = open('text2.txt', 'w')
# file.write('Новая строка')
# file.close()


# file = open('text3.txt', 'w')
# file.writelines(['str1\n', 'str2\n', 'str3\n']) # принимает список только из строк и записывает в файл
# file.close()


# file = open('numbers.txt', 'x')
# for num in range(1, 6):
#     file.write(str(num) + '\n')
# file.close()

# file = open('text4.txt', 'a')
# file.write('строка 1')
# file.close()


# image = open('bananas.jpeg', 'rb+')
# b = image.read()
# image_copy = open('banana_copy.jpeg', 'wb')
# image_copy.write(b)
# image_copy.close()
# image.close()


""" курсор """
# file = open('text1.txt', 'r')
# print(file.read())
# file.seek(0)
# print(file.read())
# file.close()

# file = open('text5.txt', 'w+')
# file.write("Моя строка для чтения")
# file.seek(0)
# print(file.read())
# file.close()


""" контекстный менеджер """
# file = open('text10.txt', 'w')
# b = 10
# file.write(b)
# print(error)
# file.close()
# try:
#     file = open('text5.txt')
#     print(error)
# finally:
#     file.close()

# with open('text5.txt', 'r') as file:
#     print(file.read())
#     print(error)

# with open('funcs.py', 'r') as code:
#     f = code.read()
#     exec(f)