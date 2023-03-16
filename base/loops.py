""" Циклы for и while """

names = ['Azat', 'Timurlan', 'Marat']
# print(len(names[0]))
# print(len(names[1]))
# print(len(names[2]))
# for name in names:
#     print(len(name))

# for промежуточная_переменная in iterable_obj:
#     тело цикла

data_types = [
    int,
    str,
    list,
    bool,
    None,
    tuple,
    set,
    dict
]
# print(dir(int))
# iter_objs = []
# non_iter_objs = []
# for type_ in data_types:
#     if '__iter__' in dir(type_):
#         iter_objs.append(type_)
#     else:
#         non_iter_objs.append(type_)
# print(iter_objs)
# print(non_iter_objs)



# nums = [10, 20, 30] # 60
# result = 0
# for num in nums:
#     result = result + num
# #     num += num
#     print(result)
# print(num)

# range()
# for i in range(11):
#     print(i)

# nums = range(5, 20, 2)
# for i in nums:
#     print(i)

# for i in range(20, 4, -1):
#     print(i)

# nums = [1, 2, 3, ...]
# nums = list(range(10))
# print(nums)
# print(range(10))
# print(list('hello world'))

# Циклы - многократное выполнение определенного участка кода

# Итерация - процесс повторения действия

# итерируемый объект - тот объект, к которому применим цикл for

# for - цикл, который работает до тех пор, пока в iter_obj не кончатся элементы


# while условие
# while - цикл, который работает до тех пор, пока условие возвращает True

# condition = 10 > 3
# # while condition is True:
# while condition:
#     print('Hello world')
    # ctrl + c


# counter = 0
# while counter < 5:
#     print('Hello world')
#     counter += 1
    # counter = counter + 1

# for i in range(5):
#     print('Hello world')


""" break, continue """
# string = 'ABCDEFG'
# for letter in string:
#     if letter == 'D':
#         break
#     print(letter)

# for i in string:
#     break
# for letter in string:
#     if letter == 'D':
#         continue
#     print(letter)   

# for letter in string:
#     if letter == 'D':
#         pass
#     else:
#         print(letter) 


# msg = input('Введите сообщение ')
# while msg != 'stop':
#     print(f'Ваше сообщение: {msg}')
#     msg = input('Введите сообщение ')

# while True:
#     msg = input('Введите сообщение ')
#     if msg == 'stop':
#         break
#     print(f'Ваше сообщение {msg}')


""" else в циклах """
# for i in range(10):
#     print(i)
# else:
#     print('Цикл успешно завершен!')

# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# else:
#     print('Цикл успешно завершен!')


# black_list = ['Don', 'Valera', 'Maksat']
# quests_q = 5
# while quests_q > 0:
#     name = input('Назовите имя ')
#     if name in black_list:
#         print('Вам нельзя!')
#         break
#     print(f'{name}, добро пожаловать!')
#     quests_q -= 1
# else:
#     print('Вечеринка начинается!')


string = 'apple'
# for i in string:
#     print(i)

counter = 0
while counter != len(string):
    print(string[counter])
    counter += 1
    # counter = counter + 1

# += - инкремент
# -= - декремент
# *=, %=, /=, //=