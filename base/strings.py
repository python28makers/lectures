""" strings (строки) """

# str()

# string - неизменямый, упорядоченным, индексируемый, итерируемым тип данных

string = 'my string'
string2 = "my string"

# string3 = 'I'm student' #Error
string4 = "I'm student"
string5 = 'I\'m student'
string6 = 'Он сказал:"I\'m student"'
# \ - символ экранирования

doc_string = """
Очень длинный
супер длинный 
текст
"""
doc_string2 = '''
Длинная 
строка
документации
'''

# +, *
# print('Hello' + 'world')
# print('Hello' + ' ' + 'world')
# Конкатенация - процесс склеивания строк

# print('Hello' * 3) # HelloHelloHello

# str1 = 'apple'
# str1 + 'potato'
# print(str1)

""" Функции и методы строк """
# print() - функция

string1 = 'Room'
# string1.capitalize()

# len(obj) - возвращает длину obj
# print(len(string1)) # 4
# len_of_string = len(string1)

# dir(obj) - возвращает список доступных методов obj
# print(dir(string1))

# Метод - функция, которая принадлежит определенному типу данных и может быть вызвана только через него (obj.some_method())

my_str = 'Hello world 1 ^'
# print(my_str.lower())
# print(my_str.upper())
# print(my_str.swapcase())

# print('artur'.capitalize())
# print('artur kanat'.capitalize())
# print('artur kanat'.title())

# print('apple,potato,carrot'.split(','))
# print('apple potato carrot'.split())

# print('korova'.replace('o', '*'))

# print(' room    '.strip())
# print('***super***'.strip('*'))
# print('   string'.lstrip())
# print('string   '.rstrip())

# print('korova'.count('o')) # 2

string = 'some string with 5 words'
# print(string.isdigit()) # False
# print('654'.isdigit()) # True
# print(string.isalpha()) # False
# print('apple'.isalpha()) # True
# print(string.isalnum()) # False
# print('apple654'.isalnum()) # True

# print(string.startswith('so')) # True
# print(string.endswith('ing')) # False

# print(string.find('o'))
# print(' '.join(['apple', 'potato', 'carrot']))

""" индексы и срезы """
# Индекс - порядковый номер элемента в строках/списках/кортежах. В программировании индексация начинается с нуля
# 'hello'
# 0 1 2 3 4
# -5 -4 -3 -2 -1
# string = 'keyword'
# print(string[3])
# print(string[-1])
# print('asodohiuglukfgasdf'[-1])

string = 'some long string'
# print(string[0:4])
start = 5
stop = 9
# print(string[start:stop])
# print(string.replace('long', '')[:])
# step = 2
# print(string[0::step])
# print(string[::-1]) 


""" Форматирование строк """
# name = input('Введите имя ')
# date = input('Введите дату')
# inv1 = '%s , приглашаю тебя на свадьбу!' % (name)
# print(inv1)
# inv2 = '{a}, приглашаю тебя на свадьбу!'.format(a=name)
# print(inv2)
# inv3 = f'{name}, приглашаю тебя на свадьбу!'
# print(inv3)

""" Символы экранирования """
# path_to_file = 'C:\\users\\new_folder'
# print('hello\nworld')
# print('hello\tworld')
# print('hello\n\tworld')
# print(path_to_file)
# print('hello\n\tworld')

