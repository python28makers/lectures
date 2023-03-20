""" comprehensions (генераторы) """

# list_ = []
# for i in range(11):
#     list_.append(i)
# print(list_)

# list_1 = [i for i in range(11)]
# print(list_1)

# comprehensions - короткий и быстрый способ создания коллекций

# пустой_список = []
# for переменная in итерируемый_объект:
#     пустой_список.append(переменная + 10) # выражение 

# синтаксис_генератора = [переменная + 10 for переменная in итерируемый объект]

""" list comprehensions """

# 1) добавить в список числа от 1 до 10
# nums = []
# for i in range(1, 11):
#     nums.append(i)
# print(nums)

# list1 = [x for x in range(1, 11)]
# print(list1)

# 2) Добавить в список числа от 1 до 10, при этом каждое число умножить на 2
# list1 = []
# for i in range(1, 11):
#     list1.append(i * 2)
# print(list1)

# list2 = [i * 2 for i in range(1, 11)]
# print(list2)

# 3) Добавить в список только четные числа из диапазона от 1 до 20 (шаг в функции range использовать нельзя)
# nums1 = []
# for i in range(1, 21):
#     if i % 2 == 0:
#         nums1.append(i)
# print(nums1)

# nums1 = [i for i in range(1, 21) if i % 2 == 0]
# print(nums1)

# синтаксис_с_условием = [переменная for переменная in итерируемый_об if условие]


# 4) Добавить в список числа от 1 до 10, при этом к четным добавлять 100, к нечетным по 400
# nums = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         nums.append(i + 100)
#     else:
#         nums.append(i + 400)
# print(nums)

# nums1 = []
# for i in range(1, 11):
#     nums1.append(i + 100 if i % 2 == 0 else i + 400)
# print(nums1)

# nums2 = [i + 100 if i % 2 == 0 else i + 400 for i in range(1, 11)]
# print(nums2)

# действие1 if условие == True else действие2 - тернарный оператор
# синтаксис_с_двумя_условиями = [тернарный оператор for переменная in итерируемый_об]

# 5) Добавить в список числа от 1 до 50. При этом к четным прибавить 100, к нечетным прибавить 400, но при этом работать с числами кратными 3
# nums = []
# for i in range(1, 51):
#     if i % 3 == 0:
#         if i % 2 == 0:
#             nums.append(i + 100)
#         else:
#             nums.append(i + 400)
#         nums.append(i + 100 if i % 2 == 0 else i + 400)

# nums1 = [i + 100 if i % 2 == 0 else i + 400 for i in range(1, 51) if i % 3 == 0]

# a = 10
# nums = a + 10 if a > 5 else 0 if a % 2 == 0 else a - 10 if a < 10 else 1
# print(nums)

""" dict comprehensions """
# names = {
#     'bakyt': 20,
#     'mirbek': 30,
#     'kanat': 21
# }
# new_names = {}
# for key, v in names.items():
#     new_names.update({key: v+1})
# print(new_names)

# new_names2 = {key:v+1 for key, v in names.items()}
# print(new_names2)

names = {
    'bakyt': 20,
    'mirbek': 30,
    'kanat': 21
}
# reversed_names = {}
# for key, value in names.items(): # ('bakyt', 20)
#     reversed_names.update({value:key})
# print(reversed_names)

# reversed_names = {value:key for key, value in names.items()}
# print(reversed_names)

""" Вложенности """
# nums = []
# for i in range(1, 11):
#     for j in range(1, 3):
#         nums.append((i, j))
# print(nums)

# nums2 = [(i, j) for i in range(1, 11) for j in range(1, 3)]
# print(nums2)

# nums3 = [[i for i in range(1, 4)] for x in range(1, 6)]
# print(nums3)



""" set and tuple comprehensions """

# set_nums = {i for i in range(1, 10)}
# print(set_nums)

# generator_nums = (i for i in range(1, 10))
# print(generator_nums)
# list_nums = [*generator_nums]
# print(list_nums)

# nums = [*range(1, 11)]
# print(nums)

# gen = (i for i in range(1, 10))
# for i in gen:
#     print(i)
# for x in gen:
#     print(x)

# iterator = range(1, 10)
# for i in iterator:
#     print(i)
# for x in iterator:
#     print(x)

# nums = tuple(i for i in range(1, 10))
# print(nums)