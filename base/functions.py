""" Функции """

# a = 10

nums = [1, 2, 3, 4, 5]
# for num in nums:
#     print(num * 2)
# nums2 = ...
# for num in nums2:
#     print(num * 2)
# nums3 = ...
# for num in nums3:
#     print(num * 2)
# nums4 = ...
# for num in nums4:
#     print(num * 2)

# print()
# max()
# pow()

# Функция - именнованный блок кода, который принимает значения, производит над ними какие-то действия и возвращает результат

'определение/создание функции'
# def имя_функции(принимаемые_значения/параметры):
#     тело_функции

'вызов функции'
# имя_функции(значения/аргументы)

# параметры - локальные переменные, объявляются при создании функции

# аргументы - значения для функции, передаются при вызове функции. Аргументов может быть столько, сколько у функции параметров

# nums1 = range(1, 10)
# nums2 = range(5, 15)

# def iterate_and_mul(x):
#     for num in x: 
#         print(num * 2)


# iterate_and_mul(nums1)
# iterate_and_mul(nums2)

# def hello():
#     print('Hello world')


# hello()
# for _ in range(10):
#     hello()

# DRY - Don't Repeat Yourself
# a = 10
# print(10) # Not Ok

# def add(x, y):
#     print(x + y)

# add(40, 50)
# add(1) # TypeError
# add(100, 200)
# add(10, 'b')


# def mul(num, num1):
#     return num * num1


# result = mul(2, 4)
# print(result)
# res2 = mul(3, 2)
# print(res2 + 10)
# print(res2 + result)

# return - ключевое слово для возвращения результата функции. Является точкой выхода из функции


# def iterate(nums):
#     for num in nums:
#         # print(num * 2)
#         return num * 2
    
# print(iterate([2, 4, 6]))

# def div(x, y):
#     return x / y
#     print('Hello world')
#     a = 10
#     print(a)

# print(div(10, 2))


# def iterate_nums(nums):
#     result = []
#     for n in nums:
#         result.append(n * 2)
#     return result
# print(iterate_nums([2, 3, 4, 5]))


""" аннотация типов """

# python - динамически типизированный
# a = 10
# str(10)
# строго типизированный
# 10 + 'string' # TypeError
# неявно типизированный
# a = 10
# c = []

# def add(a: int, b: int) -> int:
#     """
#     Эта функция нужна для сложения двух чисел
#     """
#     return a + b

# print(add(30, 20))
# print(add('string1', 'dksjs'))


# def add(a: int, b: int) -> int:
#     return a + b

# def add_and_divide(a, b, c) -> float:
#     result = add(a, b) / c
#     return result

# print(add_and_divide(10, 10, 2) + 30)

# def add(a, b=20):
#     return a + b

# add(10) # 30
# add(10, 30) # 40

# def func(a, b=10, c): # SyntaxError - параметры со значениями по умолчанию должны быть в конце
#     return a + b + c

# def func2(a=10, b=20, c=30):
#     ...

# func2()

def add_3_nums(a, b, c):
    return a + b + c

# 1. Позиционные аргументы
# add_3_nums(10, 20, 30)
# 2. Именованные аргументы
# add_3_nums(a=10, b=40, c=20)
# add_3_nums(c=20, a=22, b=10)

# add_3_nums(20, 10, c=100)

# add_3_nums(20, 10, b=100) # Error
# add_3_nums(a=10, 40, 30) # Error
# add_3_nums(10, c=20, b=30) # OK
