# 8 основных типов данных, которые делятся на 2 типа:
# 1) изменяемые типы данных
# 2) неизменяемые типы данных 

# литералы - обозначение типа данных внутри кода

# Типы данных:
# int - целые числа - 10
# float - число с плавающей точкой - 10.5
# complex - число с буквенным выражением - 537618n
# str - строковый тип данных - 'строка', "строка"
# bool - булевый/логический тип данных - True/False
# list - список - [1, 2, 3]
# tuple - кортеж/неизменяемый список - (1, 2, 3)
# set - множество уникальных элементов - {1, 2, 3}
# dict - словарь - {1: 2}
# None - тип данных для обозначения пустоты

# изменяемые:
# 1) list
# 2) dict
# 3) set

# a = 10 + 10
# print(a)

# однострочный комментарий
"""  
Многострочный
очень длинный
комментарий
"""

""" Переменные """
# a = 10 # Ok
# !%$&var = 10 # Error
# 18var = 39 # Error
# Название переменной не должно начинаться со спец символов и цифр

my_var = 10 # snake_case
myVar = 10 # camelCase

# my-var = 10 # Error
# my var = 10 # Error

# Название переменной не должно совпадать с названиями ключевых слов в Python
# print = 20
# print() # Error

MY_CONST = 30 # Константа

# l = 
# o = 

# Давайте своим переменным осмысленные имена 
# a = 10 # Not ok
# num = 10 # Ok

""" Функции для вывода(print) и ввода(input) данных в терминал/консоль """

# print(1) # выводит информацию в терминал
# print(1, 2, 3)

# input() # функция для ввода данных в терминал
# msg = input()
# print(msg)

# num = int(input())
# print(num + 10)
#     # '20' + 10 

# str_num = '200'
# print(int(str_num) + 70)

# int_num = 80
# print(str(int_num)) # '80'

# a = '40'
# print(type(a))

