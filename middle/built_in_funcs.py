""" Встроенные функции """

"""  
map()
filter()
reduce()
zip()
enumerate()
all()
any()
eval()
exec()
"""

# map(func, *итер_объекты)

# def mul(num):
#     return num * 2

# nums = [1, 2, 3, 4, 5]
# new_nums = list(map(mul, nums))
# print(new_nums)

# names = ['Azamat', 'Dinara', 'Adilet', 'Aliya']
# len_of_names = list(map(len, names))
# print(len_of_names)


# names_2 = {'Azamat': 6, 'Dinara': 6, 'Adilet': 6, 'Aliya': 5}
# def add_num(name):
#     return (name[0],name[1] + 20) # ('Azamat', 6)
# new_names2 = dict(map(add_num, names_2.items()))
# print(new_names2)

# lambda - ключевое слово для создания анонимных функций
# def func_name(x):
#     return x + 10

# func_name2 = lambda x: x + 10
# func_name(20) # 30 
# func_name2(40) # 50

# strings = ['apple', 'potato', 'carrot', 'pineapple']
# def my_upper(s: str):
#     return s.upper()
# upper_strings = map(my_upper, strings)
# up_strings = map(lambda s: s.upper(), strings)
# print(list(upper_strings))
# print(tuple(up_strings))


""" filter() """
# filter(func -> bool, итер_объект)
# nums = range(1, 40)
# even_nums = filter(lambda x: x % 2 == 0, nums)
# print(list(even_nums))


# random_string = 'SasdfjASODojiwefASDOJASDOJrefjefASDlk'
# lower_cases = filter(lambda s: s.islower(), random_string)
# joined_string = ''.join(lower_cases)
# print(joined_string)
# print(list(lower_cases))

# types = [0, False, '', 1, 'asd', [], None]
# trues = filter(None, types)
# print(list(trues))


""" reduce() """
# from functools import reduce
# reduce(func, итер_объекты)

# nums = [1, 2, 3, 4, 5]
# summ = reduce(lambda x, y: x + y, nums)
# print(summ)

""" zip() """
# zip(*итер_объекты)
# names = ['Malik', 'Aydana', 'Azret', 'Grigoriy']
# ages = [20, 21, 18, 15]
# names_with_age = dict(zip(names, ages))
# print(names_with_age)

# a1 = ['a', 'b', 'c', 'd']
# b1 = [1, 2, 3, 4, 5, 6]
# c1 = ['apple', 'potato', 'watermelon']
# zipped = zip(a1, b1, c1)
# print(list(zipped))


""" enumerate() """
# enumerate(итер_объект, [start])
# list_1 = ['apple', 'computer', 'human', 'hand']
# new_list = list(enumerate(list_1))
# print(new_list)

# num_list = dict(enumerate(list_1, start=10))
# print(num_list)

# names = ['Sezim', 'Mirdin', 'Kylych']
# for index, name in enumerate(names):
#     if index == 1:
#         names[index] = 'Salamat'
# print(names)


""" all(), any() """
# all(итер_объект)

# data = [True, True, True]
# print(all(data)) # True
# print(all([True, False, True])) # False
# print(all([2, 3, 1, 0, 10])) # False
# print(all(i.islower() for i in 'jhasdgHGh')) # False

# data = [True, True, True]
# print(any(data)) # True
# print(any([False, False, False, True])) # True
# print(any(i for i in input('Введите пароль ') if i in ';.^&%$'))


""" eval(), exec() """
# eval(выражение)

# eval("print('Hello world')")
# eval(f"print({int(input('1 ' ))} {input('оператор ')} {int(input('2 ' ))})")


# code = """
# for i in range(1, 10):
#     print(i)
# """
# exec(code)

