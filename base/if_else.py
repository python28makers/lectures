""" Условные выражения """
# if условие1:
#     действие, если условие1 Истина
# else:
#     действие, если if не сработал

# bool() - неизменяемый, имеет всего 2 значения - True/False

num = 10
num2 = 5
num > num2 # True
num < num2 # False
num == num2 # False
num != num2 # True
num >= num2 # True
num <= num2 # False

print(bool(1)) # True
print(bool(0)) # False

# if asdffs
# if bool(asdfasd)

# print(bool('hello')) # True
# bool('') # False
# bool([])
# bool({})
# bool(0)
# bool(None)

""" if """
# temp = 13
# if temp > 15: 
#     print('Тепло')

# temp = 20
# if temp < 15:
#     print('Прохладно')
# else:
#     print('Тепло')


# temp = 25
# if temp < 15:
#     print('Прохладно')
# elif temp == 25:
#     print('Идеально')
# else:
#     print('Жарко')

# num2 = 10
# if num == 10:
#     print('Ок')
# if num > 5:
#     print('Ок2')

# num = 10
# if num > 5:
#     print('num > 10')
# elif num < 5:
#     print('num < 10')

# if 'hello':
#     print('working')

# if bool('hello') == True:
#     print('working')

""" and, or, not """
# age = 20
# if age > 18 and age < 40:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')

False # False
True # True
True and True # True
False and False # False
False and True # False
True and False # False
# условие and условие2 - оператор and требует, чтобы оба условия были True, иначе False

# условие or условие2 - or требует, чтобы ХОТЯ бЫ ОДНО условие было True 
False or False # False
True or True # True
False or True # True
True or False # True

not True # False
not False # True

(True and False) or (False or True) # True
(True or False) and (False and True) # False


""" ==, is """
# a = 10
# b = 10
# print(a == b)
# print(a is b)
# print(id(a))
# print(id(b))

""" in """
# коллекции: списки, словари, кортежи, строки, множества
string = 'potato'
print('t' in string) # True

# in - проверка на вхождение 

""" Тернарный оператор """
# действие1 if условие else действие2
num = 10
result = "num > 10" if num >= 10  else "num < 10"
print(result)

# login = 'my_username123'
# password = 'mySuperpassword123'
# if input('Введите логин ') == login and input('Введите пароль ') == password:
#     print('Welcome!')
# else:
#     print('Неправильный логин или пароль')

""" сравнение строк, таблица ASCII """
print('hello' > 'hello')
print(ord('A')) # 65 в таблице ASCII
print(chr(72)) # 'H' в таблице ASCII