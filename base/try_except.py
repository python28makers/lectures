""" Исключения и ошибки """

# исключение - проблема в логике работы кода
# ошибка - проблема в написании кода


# Exception - родитель исключений

# a = 10
# b = 30
# print(c)
NameError # исключение имени


# 10 / 0
ZeroDivisionError # деление на ноль


# nums = [1, 2, 3]
# nums[78]
IndexError # исключение индекса 


names = {'kalys': 10, 'ansar': 5}
# names['aliya']
KeyError # исключение ключа


# num = 10
# num + 'string'
TypeError # исключение типов данных, когда тип данных не подходит для операции


num = '10'
int(num) # ok
int(20) # ok
int(10.05) # ok
# int('string') #
ValueError # когда тип данных подходит для операции, но значение - нет
from math import sqrt
sqrt(25) # 5
# sqrt(-20) 


string = 'string'
# string.append('a')
AttributeError # отсутствие атрибута или метода у объекта

# import math
# import maz
# ModuleNotFoundError

# from math import wrong_func
ImportError


SyntaxError
# for i in range(10)
#     print(i)

# for i in range(10):
# print(i)
IndentationError # ошибка отступов


# while True:
#     print(12)
# ctrl + c - KeyboardInterrupt


""" try except """
# contacts = {
#     'Zeynep': 996848393029,
#     'Atabek': 82719278473
# }
# print('Контакты сохранены')
# contacts['Bekzat']
# print('Hello world')
# print(2 + 2)

# contacts = {
#     'a': 3484,
#     'b': 9382
# }
# try:
#     contacts['c']
# except:
#     print('Нет такого ключа')
# print('Hello world')
# print(2 + 2)

# try: # выполняет код с потенциальным исключением
#     print('some code')
# except: # отлавливает исключение из блока try
#     print('что-то пошло не так')
# else: # срабатывает, если try прошел без исключений
#     print('try прошел без ошибок')
# finally: # код, который сработает в любом случае
#     print('сработаю в любом случае')

# исключения обрабатываются с помощью try-except, а ошибки - нет

# try:
#     ...
# except: # голое исключение
#     ...

nums = [1, 2, 3]
# try:
#     nums[10]
#     print(c)
# except:
#     print('что-то пошло не так')

# try:
#     nums[10]
#     print(c)
# except IndexError:
#     print('Неверно указан индекс')
# except NameError:
#     print('Неправильная переменная')

# try:
#     a = 10
#     a / 0
#     a.upper()
# except (ZeroDivisionError, AttributeError):
#     print('Деление на ноль или ошибка атрибута')


# try:
#     10 / 0
# except Exception as error:
#     print(error)


""" raise """

# raise - ключевое слово для поднятия/вызова исключений
# money = 0
# if money == 0:
#     raise ValueError('Недостаточно денег')

# try:
#     raise Exception('ОШИБКА!')
# except Exception as e:
#     print(e)


# contacts = {'Aidai': 99685849403, 'Aliya': 9964638292}
# try:
#     name = input('Введите имя ').title().strip()
#     print(f'Звоним {contacts[name]}')
# except KeyError:
#     print('Нет такого имени')
# finally:
#     print('Программма завершила работу')


# contacts = {'Aidai': 99685849403, 'Aliya': 9964638292}
# name = input('enter the name ').title()
# if name not in contacts:
#     print('Нет такого имени')
# else:
#     print(f'Звоним {contacts[name]}')


count = 0
while True:
    try:
        num = int(input('Ввести число '))
    except ValueError:
        print('Введи число, а не строку')
    else:
        count += num
    finally:
        print(count)
        if count > 50:
            raise Exception('Число достигло максимума')